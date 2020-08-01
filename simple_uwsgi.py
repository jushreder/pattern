'''
uwsgi
'''
from page_controllers import Index_view, Catalog_view, not_found_404_view, Contact
from front_controllers import user_key, secret_key
from datetime import datetime
from loger import logger


ROUTES = {
    '/': Index_view(),
    '/catalog/': Catalog_view(),
    '/contact/': Contact()
}
# front controllers
FRONT_CONTROLLER = [
    user_key,
    secret_key
]


class App:
    '''
    app
    '''

    def __init__(self, routes, front_controllers):
        self.urls = routes
        self.fronts = front_controllers

    def __call__(self, environ, start_responce):
        path = environ['PATH_INFO']
        logger.debug(f"{datetime.today().strftime('%Y-%m-%d %H:%M:%S')}, {path}")

        if not path.endswith('/'):
            path +='/'
        view = not_found_404_view
        if path in self.urls:
            view = self.urls[path]
        request = {}
        for front in self.fronts:
            front(request)
        code, respons = view(request)
        start_responce(code, [('Content-Type', 'text/html')])
        return respons


application = App(ROUTES, FRONT_CONTROLLER)
