'''
uwsgi
'''
import quopri
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


def get_post_data(environ):
    length_data = int(environ.get('CONTENT_LENGTH'))
    data = environ['wsgi.input'].read(length_data) if length_data > 0 else b''
    return data


def parse_input_data(data):
    '''
    parse_input_data
    '''
    result = {}
    if data:
        params = data.split('&')
        for item in params:
            # делим ключ и значение через =
            k, v = item.split('=')
            v = v.replace('%', '=')
            v = quopri.decodestring(v)
            result[k] = v.decode('utf-8').replace('+',' ')
        return result

def parse_data(data):
    result = {}
    if data:
        result = parse_input_data(data.decode('utf-8'))
    return result


class App:
    '''
    app
    '''

    def __init__(self, routes, front_controllers):
        self.urls = routes
        self.fronts = front_controllers

    def __call__(self, environ, start_responce):
        date = datetime.today().strftime('%Y-%m-%d %H:%M:%S')

        path = environ['PATH_INFO']
        logger.debug(f"{date}, {path}")

        request_params = parse_input_data(environ['QUERY_STRING'])
        if environ['QUERY_STRING']:
            logger.debug(f"{date}, {request_params}")
            print(request_params)

        if environ['REQUEST_METHOD'] == 'POST':
            data_bytes = get_post_data(environ)
            data = parse_data(data_bytes)
            logger.debug(f"{date}, POST {data}")
            print(data)


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
