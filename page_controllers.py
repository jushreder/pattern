'''
 modul page controller
 '''

from templator import render


class Index_view:
    '''
    view page index
    :param:
    :return:
    '''

    def __call__(self, request):
        content = {}
        content['title'] ='Главная'
        content['request'] = request
        return '200 OK', [render('index.html', content)]


class Catalog_view:
    def __init__(self):
        self.object_list = [{'name': 'Boris'}, {'name': 'Doris'}]


    def __call__(self, request):
        content ={}
        content['title']= 'Каталог'
        content['data'] = self.object_list
        return '200 OK', [render('catalog.html', content)]


def not_found_404_view(request):
    '''
    view page not_found_404
    :param:
    :return:
    '''
    return '404 Not Found', [b'<h1>404 Page Not Found</h1>']


class Contact:
    '''
    view page Product
    '''
    def __init__(self):
        self.object_list = [{'name': 'Boris'}, {'name': 'Doris'}]

    def __call__(self,request):
        content = {}
        content['title']= 'Контакты'
        return '200 OK', [render('contacts.html', content)]
