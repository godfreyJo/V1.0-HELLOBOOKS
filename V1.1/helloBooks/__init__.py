from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail
from helloBooks.config import Config






db = SQLAlchemy()
bcrypt = Bcrypt()
login_manager = LoginManager()
login_manager.login_view = 'users.login'
login_manager.login_message_category = 'info'
mail = Mail()




def create_app(config_class=Config):
	app = Flask(__name__)
	app.config.from_object(Config)

	db.init_app(app)
	bcrypt.init_app(app)
	login_manager.init_app(app)
	mail.init_app(app)

	from helloBooks.users.routes import users
	from helloBooks.books.routes import books
	from helloBooks.main.routes import main
	from helloBooks.errors.handlers import errors
	app.register_blueprint(users)
	app.register_blueprint(books)
	app.register_blueprint(main)
	app.register_blueprint(errors)

	return app


