from flask import render_template, url_for, flash, redirect
from helloBooks import app
from helloBooks.forms import RegistrationForm, LoginForm
from helloBooks.models import User, Book


books = [
    {
        'title': 'Microeconomics',
        'bookowner': 'Wenger B',
        'author': 'Corey Schafer',
        'content': 'First post content',
        'date_posted': 'April 20, 2018'

    },
    {
        'title':'Primary English',
        'bookowner': 'Wenger B',
        'author': 'Greg Norman',
        'content': 'Basic English...',
        'date_posted': 'May 20, 2019'},

    {
        'title':'Primary Maths',
        'bookowner': 'Wenger B',
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