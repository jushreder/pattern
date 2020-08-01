'''
templater
'''
from jinja2 import Environment, FileSystemLoader  # , Template


def render(file, object_list):
    '''
    render page
    :param file:
    :param object_list:
    :return:
    '''
    loader_new = FileSystemLoader('templates')
    env = Environment(loader=loader_new)

    template = env.get_template(file)

    render_str = template.render(object_list=object_list)
    return render_str.encode(encoding='UTF-8')

# def render(template_name, object_list):
#     with open(template_name, encoding='utf_8') as file:
#         template = Template(file.read())
#         return template.render(object_list)


if __name__ == '__main__':

    TEST = render('index.html', object_list=[{'name': 'Boris'}, {'name': 'Doris'}])
    print(TEST)
