from datetime import datetime
from flask import Flask, render_template, url_for, flash, redirect
from flask_sqlalchemy import SQLAlchemy
from forms import RegistrationForm, LoginForm


app = Flask(__name__)
app.config['SECRET_KEY'] = '67397d27f41e16d65a3d00e10112b4e0'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///HelloBooksWebsite.db'

db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False. default='default.jpg')
    password = db.Column(db.String(60),  nullable=False)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), unique=True, nullable=False)
    author = db.Column(db.String(20), unique=True, nullable=False)
    date_posted = db.Column(db.DateTime, unique=True, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f"User('{self.title}', '{self.author}')"

books = [
    {
        'title': 'Microeconomics',
        'author': 'Corey Schafer',
        'content': 'First post content',
        'date_posted': 'April 20, 2018'

    },
    {
        'title':'Primary English',
        'author': 'Greg Norman',
        'content': 'Basic English...',
        'date_posted': 'May 20, 2019'},

    {
        'title':'Primary Maths',
        'author': 'Robina Hera',
        'content': 'First post content',
        'date_posted': 'April 20, 2018'}
    ]





@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', books=books)


@app.route("/about")
def about():
    return render_template('about.html', title='About')


@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.email.data == 'admin@hbook.com' and form.password.data == 'password123':
        flash('You have been logged in!', 'success')
        return redirect(url_for('home'))
    else:
        flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)


if __name__ == '__main__':
    app.run(debug=True)
