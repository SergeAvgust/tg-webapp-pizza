from views import *
from aiohttp.web import Application
from settings import BASE_DIR

def setup_routes(app: Application):
    app.router.add_get('/webapp', webapp)
    app.router.add_get('/', index)

def setup_static_routes(app: Application):
    app.router.add_static('/static/',
                          path=BASE_DIR / 'tgserver' / 'static',
                          name='static')