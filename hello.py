'''
------------------------
how to run from terminal
-------------------------
set FLASK_APP=filename.py
flask run

for example:
set FLASK_APP=hello.py
flask run

--------------------------------------
how to run .py file in a sub directory
---------------------------------------
set FLASK_APP=folder:filename
flask run

for example:
set FLASK_APP=TWITOFF:APP
flask run

'''

from flask import Flask, render_template
#create Flask web server, makes the application
app = Flask(__name__)
#routes determine location
@app.route("/")
#Define simple function
def home():
    return render_template('home.html')

@app.route("/about")
def preds():
    return render_template('about.html')

