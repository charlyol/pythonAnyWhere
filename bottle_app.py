
# A very simple Bottle Hello World app for you to get started with...
from bottle import default_app, route, run


@route('/')
def hello_world():
    return 'truitze \n 15648643645 \n 5189181561'


application = default_app()

if __name__ == '__main__':
    run()
