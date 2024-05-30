# A very simple Bottle Hello World app for you to get started with...
from bottle import default_app, route, run, template, request
from diamond import create_diamond


@route('/')
def home():
    # Get the letter from the query parameters
    letter = request.query.get('letter', '')

    # Generate the diamond using the provided letter
    diamond_result = create_diamond(letter)

    # Render the template with the diamond result
    return template('home_page', diamond_result=diamond_result)


application = default_app()

if __name__ == '__main__':
    run()
