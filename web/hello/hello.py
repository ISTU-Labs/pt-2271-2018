from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.response import Response
from pkg_resources import resource_filename
from collections import namedtuple
from sqlalchemy.orm import sessionmaker
from database import init, User, Recipe, SESSIONMAKER, ENGINE, CREATE_ENG
from pyramid.httpexceptions import HTTPFound
from dateutil import parser
from sqlalchemy.orm.attributes import set_attribute

# RESPONSE
# ^
# REQUEST (GET, PUT, POST, DELETE, HEAD....), URL
# Model, (MVC, MVP).

from datetime import datetime


def ImportDB():
    import csv

    filename = resource_filename("hello", "data/data.csv")

    init()

    print("CSV filename: ", filename)
    csv_data = csv.reader(open(filename),
                          delimiter=";",
                          quoting=csv.QUOTE_NONE)
    fields = next(csv_data)
    # Emp = namedtuple('Emp', fields+['number'])

    session = SESSIONMAKER()

    def MakeUser(name, email, tel, date, comp):
        return User(name=name,
                    email=email,
                    tel=tel,
                    # date=parser.parse(date),
                    comp=comp)

    for row in csv_data:
        user = MakeUser(*row)
        session.add(user)

    session.commit()
    print(session)

    print(session.query(User).first())
    session.close()


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
        session = self.request.db

        query = session.query(User)

        id = self.id

        rows = None

        if id is not None:
            user = query.filter_by(id=id).first()
            print(user)

            def user_it():
                yield user

            rows = user_it()
        else:
            rows = query

        for row in rows:
            print(row)

        session.close()
        return rows

    data = property(get_data)

    def __call__(self, **params):
        if self.request is None:
            raise RuntimeError("this method cannot be tested")

        answer = {"view": self,
                  "request": self.request,
                  #          "context": self.context
                  }
        answer.update(params)
        return answer

    def get_emp(self):
        session = self.request.db
        user = session.query(User).filter_by(id=self.id).first()
        return user

    emp = property(get_emp)


def hello_world(request):

    view = HelloView(request=request,
                     title="Hi again!")

    return view(copy="Students of ISU, 2018")


def view_row(request):
    view = HelloView(request=request,
                     title="Edit record",
                     id=request.GET.get("id"))
    return view(subtitle="An extraordinary student of our university")


def save_user(request):
    id = request.POST.get("id")

    session = request.db
    user = session.query(User).filter_by(id=id).first()
    for name in request.POST.keys():
        if name == "date":
            continue
        if hasattr(user, name):
            val = request.POST.get(name)
            set_attribute(user, name, val)

    user.date = parser.parse(request.POST.get("date"))
    print(user)
    session.add(user)
    session.commit()

    return HTTPFound(location=request.application_url+"/view?id="+id+"&msg=User+updated")


def main(global_config, **settings):
    def db(request):
        maker = request.registry.dbmaker
        session = maker()

        def cleanup(request):
            if request.exception is not None:
                session.rollback()
            else:
                session.commit()
            session.close()

        request.add_finished_callback(cleanup)

        return session

    with Configurator(settings=settings) as config:

        engine = CREATE_ENG()  # engine_from_config(settings, prefix='sqlalchemy.')
        config.registry.dbmaker = sessionmaker(bind=engine)
        config.add_request_method(db, reify=True)

        config.add_route('hello', '/')
        config.add_view(hello_world, route_name='hello',
                        renderer='hello:templates/index.pt')

        config.add_route('view_emp', '/view')
        config.add_view(view_row, route_name='view_emp',
                        renderer='hello:templates/view.pt')

        config.add_route('save_user', '/save')
        config.add_view(save_user, route_name='save_user')

        config.add_static_view(name='css', path='hello:templates/css')
        config.add_static_view(
            name='fonts', path='hello:templates/fonts')
        config.add_static_view(name='img', path='hello:templates/img')
        config.add_static_view(name='js', path='hello:templates/js')
        config.add_static_view(name='scss', path='hello:templates/scss')
        app = config.make_wsgi_app()

    ImportDB()

    return app


if __name__ == '__main__':
    PORT = 6543
    app = main(None, {})
    server = make_server('0.0.0.0', PORT, app)
    server.serve_forever()
