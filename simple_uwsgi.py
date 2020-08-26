'''
uwsgi
'''
import quopri
from datetime import datetime
from loger import logger


class App:
    '''
    app
    '''

    def parse_data(self, data):
        result = {}
        if data:
            result = self.parse_input_data(data.decode('utf-8'))
        return result

    def get_post_data(self, environ):
        length_data = int(environ.get('CONTENT_LENGTH'))
        data = environ['wsgi.input'].read(
            length_data) if length_data > 0 else b''
        return data

    def parse_input_data(self, data):
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
                result[k] = v.decode('utf-8').replace('+', ' ')
            return result

    def not_found_404_view(request):
        return '404 Not Found', '<h3>404 Page Not Found</h3>'

    def __init__(self, routes, front_controllers):
        self.urls = routes
        self.fronts = front_controllers

    def __call__(self, environ, start_responce):
        date = datetime.today().strftime('%Y-%m-%d %H:%M:%S')
        request = {}
        request['method'] = environ.get('REQUEST_METHOD')
        for front in self.fronts:
            front(request)
        if request['method'] == 'POST':
            data_bytes = self.get_post_data(environ)
            request['data'] = self.parse_data(data_bytes)

        if environ['QUERY_STRING']:
            request['params'] = self.parse_input_data(environ['QUERY_STRING'])
            logger.debug(f"{date}, {request['params']}")

        path = environ['PATH_INFO']
        if not path.endswith('/'):
            path += '/'

        logger.debug(f"{date}, {path}")


        view = self.not_found_404_view
        if path in self.urls:
            view = self.urls[path]
        code, respons = view(request)
        start_responce(code, [('Content-Type', 'text/html')])
        return [respons.encode('UTF-8')]
