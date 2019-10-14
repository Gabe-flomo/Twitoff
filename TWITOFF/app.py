''' Main application for twitoff '''

# imports 
from flask import Flask
#from .models import DB

#create app factory
def create_app():
    ''' creates and configures an instance of a flask app '''
    app = Flask(__name__)

    #app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'

    @app.route("/")
    def root():
        return "Welcome to our app"
    return app
    