from wsgiref.simple_server import make_server

from pyramid.config import Configurator
from waitress import serve

if __name__ == "__main__":
    with Configurator() as config:
        config.include('pyramid_debugtoolbar')
        config.add_static_view(name='static', path='static')
        config.add_route("users", "/users")
        config.add_route("user", "/users/{user_id}")
        config.scan("views")
        app = config.make_wsgi_app()
    server = make_server('0.0.0.0', 6543, app)
    server.serve_forever()
