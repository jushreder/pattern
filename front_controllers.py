'''
front conroller
'''


def user_key(request):
    '''
    user_key
    :param request:
    :return:
    '''
    request['user_key'] = 'user_key'


def secret_key(request):
    '''
    secret_key
    :param request:
    :return:
    '''
    request['secret_key'] = 'secret_key'
