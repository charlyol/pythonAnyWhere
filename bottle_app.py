
# A very simple Bottle Hello World app for you to get started with...
from bottle import default_app, route, run, template


@route('/')
def hello_world():
    return template('home_page')


application = default_app()

if __name__ == '__main__':
    run()
