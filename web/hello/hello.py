from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.response import Response
from pkg_resources import resource_filename

# RESPONSE
# ^
# REQUEST (GET, PUT, POST, DELETE, HEAD....), URL
# Model, (MVC, MVP).

from datetime import datetime
import csv

filename = resource_filename("hello", "data/data.csv")

print("CSV filename: ", filename)


class HelloView(object):
    def __init__(self, title="Hi!"):
        self.title = title

    def get_now(self):
        return datetime.now().strftime("%b %d %Y %H:%M:%S")

    now = property(get_now)

    def get_data(self):
        csv_data = csv.reader(filename)
        next(csv_data)
        return csv_data

    data = property(get_data)


def hello_world(request):
    view = HelloView(title="Hi again!")
    print("I'm here!")
    return {"view": view, "request": request}


def main(global_config, **settings):
    with Configurator(settings=settings) as config:
        config.add_route('hello', '/')
        config.add_view(hello_world, route_name='hello',
                        renderer='hello:templates/index.pt')
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
