from flask import Flask
from flask_sqlalchemy import SQLAlchemy





app = Flask(__name__)
app.config['SECRET_KEY'] = '67397d27f41e16d65a3d00e10112b4e0'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///HelloBooksWebsite.db'
db = SQLAlchemy(app)

from helloBooks import routes