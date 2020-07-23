from flask import Flask
from snakeeyes.blueprints.page import page

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

    app.register_blueprint(page)
    
    return app
    