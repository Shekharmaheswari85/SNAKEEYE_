from flask import Flask


def create_app():
    """
    Create a Flask application using the app factory pattern.

    :return: Flask app
    """
    app = Flask(__name__, instance_relative_config=True)  
    '''
    instance_relative_config will tell the application
    to look for configuration in the 
    settings.py on the instance varible file
    '''

    app.config.from_object('config.settings')
    app.config.from_pyfile('settings.py', silent=True)

    @app.route('/')
    def index():
        """
        Render a Hello World response.

        :return: Flask response
        """
        return app.config['HELLO']

    return app
