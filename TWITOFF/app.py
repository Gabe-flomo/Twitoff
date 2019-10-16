''' Main application for twitoff '''

# imports 
from flask import Flask, render_template, request
from decouple import config
from .models import DB, User

#create app factory
def create_app():
    ''' creates and configures an instance of a flask app '''
    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = config('DATABASE_URL')
    app.config['ENV'] = config('ENV') #should change this later to production
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS']= False
    DB.init_app(app)

    @app.route("/")
    def root():
        user = User.query.all()
        return render_template('base.html', title = "home",user = user)
    return app
    