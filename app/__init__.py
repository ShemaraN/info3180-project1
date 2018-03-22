from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = "change this to be a more random key"
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://agewwbscoyzgpd:c441d652dfc08b417c9756990a5e17c7dc86e693f117cd2d7f0a7bba94efd1d6@ec2-107-20-233-240.compute-1.amazonaws.com:5432/dddrsuh0n02j25'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True # added just to suppress a warning
app.config['UPLOAD_FOLDER']= "./app/static/uploads" # using a config value

db = SQLAlchemy(app)


app.config.from_object(__name__)
from app import views
