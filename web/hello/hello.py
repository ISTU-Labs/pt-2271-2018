from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.response import Response
from pkg_resources import resource_filename
from collections import namedtuple
from database import init, User, Recipe, SESSION

# RESPONSE
# ^
# REQUEST (GET, PUT, POST, DELETE, HEAD....), URL
# Model, (MVC, MVP).

from datetime import datetime
import csv

filename = resource_filename("hello", "data/data.csv")

init()


print("CSV filename: ", filename)
csv_data = csv.reader(open(filename),
                      delimiter=";",
                      quoting=csv.QUOTE_NONE)
fields = next(csv_data)
# Emp = namedtuple('Emp', fields+['number'])


def MakeUser(name, email, tel, date, comp):
    return User(name=name,
                email=email,
                tel=tel,
                # date=date,
                comp=comp)


for row in csv_data:
    user = MakeUser(*row)
    SESSION.add(user)

SESSION.commit()
print(SESSION)


class HelloView(object):
    def __init__(self,
                 request=None,
                 title="Hi!",
                 id=None):
        self.title = title
        if id is not None:
            self.id = int(id)  # FIXME: Check integer type
        else:
            self.id = id
        self.request = request

    def get_now(self):
        return datetime.now().strftime("%b %d %Y %H:%M:%S")

    now = property(get_now)

    def get_data(self):
        print(SESSION)

        query = SESSION.query(User)

        id = self.id

        if id is not None:
            user = query.filter_by(id=id).first()

            def numbered_data(csv_data):
                yield user
        else:
            def numbered_data(csv_data):
                yield from query

        return numbered_data(csv_data)

    data = property(get_data)

    def __call__(self, **params):
        if self.request is None:
            raise RuntimeError("this method cannot be tested")

        answer = {"view": self, "request": self.request}
        answer.update(params)
        return answer

    def get_emp(self):
        return next(self.data)

    emp = property(get_emp)


def hello_world(request):
    view = HelloView(request=request,
                     title="Hi again!")
    # print("I'm here!")

    return view(copy="Students of ISU, 2018")


def view_row(request):
    view = HelloView(request=request,
                     title="Edit record",
                     id=request.GET.get("id"))
    return view(subtitle="An extraordinary employee of our university")


def main(global_config, **settings):
    with Configurator(settings=settings) as config:

        config.add_route('hello', '/')
        config.add_view(hello_world, route_name='hello',
                        renderer='hello:templates/index.pt')

        config.add_route('view_emp', '/view')
        config.add_view(view_row, route_name='view_emp',
                        renderer='hello:templates/view.pt')

        config.add_static_view(name='css', path='hello:templates/css')
        config.add_static_view(
            name='fonts', path='hello:templates/fonts')
        config.add_static_view(name='img', path='hello:templates/img')
        config.add_static_view(name='js', path='hello:templates/js')
        config.add_static_view(name='scss', path='hello:templates/scss')
        app = config.make_wsgi_app()

    return app


if __name__ == '__main__':
    PORT = 6543
    app = main(None, {})
    server = make_server('0.0.0.0', PORT, app)
    server.serve_forever()
