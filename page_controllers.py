'''
 modul page controller
 '''
import json
from templator import render
from loger import logger

class Index_view:
    '''
    view page index
    :param:
    :return:
    '''

    def __call__(self, request):
        content = {}
        content['title'] = 'Главная'
        content['request'] = request
        return '200 OK', render('index.html', content)


class Catalog_view:
    def __init__(self):
        self.object_list = [{'id': 1, 'name': 'Boris'},
                            {'id': 2, 'name': 'Doris'}]

    def __call__(self, request):
        content = {}
        content['title'] = 'Каталог'
        content['data'] = self.object_list
        return '200 OK', render('catalog.html', content)


class Contact:
    '''
    view page Product
    '''

    def __init__(self):
        with open('contacts.json') as file:
            row = file.read()
            self.object_list = json.loads(row)

    def __call__(self, request):
        content = {}
        if request['method'] == 'POST':
            with open('message.json', 'w') as file:

                file.write(
                    json.dumps(
                        request['data'],
                        ensure_ascii=False,
                        indent=2))
            print(request['data'])
            content['title'] = 'Главная'
            return '200 OK', render('index.html', content)

        else:
            content['title'] = 'Контакты'
            content['data'] = self.object_list
            return '200 OK', render('contacts.html', content)
