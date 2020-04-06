from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager





app = Flask(__name__)
app.config['SECRET_KEY'] = '67397d27f41e16d65a3d00e10112b4e0'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///HelloBooksWebsite.db'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)

from helloBooks import routes