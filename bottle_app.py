
# A very simple Bottle Hello World app for you to get started with...
from bottle import default_app, route, run


@route('/')
def hello_world():
    return 'fuck hello world épisode 2 i will be back!'


application = default_app()

if __name__ == '__main__':
    run()
