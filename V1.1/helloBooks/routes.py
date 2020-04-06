from flask import render_template, url_for, flash, redirect
from helloBooks import app, db, bcrypt
from helloBooks.forms import RegistrationForm, LoginForm
from helloBooks.models import User, Book
from flask_login import login_user, current_user, logout_user, login_required



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
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash(f'Your account has been created: You are now able to buy and read our collection of Books!', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')                     
        
    return render_template('login.html', title='Login', form=form)


    app.route("/logout")
def logout():