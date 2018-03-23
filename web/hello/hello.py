from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.response import Response

# RESPONSE
# ^
# REQUEST (GET, PUT, POST, DELETE, HEAD....), URL
# Model, (MVC, MVP).


i = open("hello/template/index.html")
TEMPLATE = i.read()
i.close()


def hello_world(request):
    answer = TEMPLATE
    return Response(answer)


def main(global_config, **settings):
    with Configurator(settings=settings) as config:
        config.add_route('hello', '/')
        config.add_view(hello_world, route_name='hello')
        app = config.make_wsgi_app()

    return app


if __name__ == '__main__':
    PORT = 6543
    app = main(None, {})
    server = make_server('0.0.0.0', PORT, app)
    server.serve_forever()
