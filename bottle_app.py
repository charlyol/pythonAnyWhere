
# A very simple Bottle Hello World app for you to get started with...
from bottle import default_app, route, run, template, TEMPLATE_PATH
import os

path_directory = os.path.join(os.getcwd(), 'views')
TEMPLATE_PATH.insert(0, path_directory)


@route('/')
def hello_world():
    return template('home_page')


application = default_app()

if __name__ == '__main__':
    run()
