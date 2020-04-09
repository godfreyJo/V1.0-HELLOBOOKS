import os
import secrets
from PIL import Image
from flask import render_template, url_for, flash, redirect, request, abort
from helloBooks import app, db, bcrypt
from helloBooks.forms import RegistrationForm, LoginForm, UpdateProfileForm, BookForm
from helloBooks.models import User, Book
from flask_login import login_user, current_user, logout_user, login_required





@app.route("/")
@app.route("/home")
def home():
    books = Book.query.all()
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
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')                     
        
    return render_template('login.html', title='Login', form=form)


@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('home'))

def save_picture(form_picture):
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(app.root_path, 'static/profile_pics', picture_fn)
    output_size = (125,125)
    i = Image.open(form_picture)
    i.thumbnail(output_size)
    i.save(picture_path)

    return picture_fn





@app.route("/profile", methods=['GET', 'POST'])
@login_required   
def profile():
    form = UpdateProfileForm()
    if form.validate_on_submit():
        if form.picture.data:
            picture_file = save_picture(form.picture.data)
            current_user.image_file = picture_file
        current_user.username = form.username.data
        current_user.email = form.email.data
        db.session.commit()
        flash('Your account has been updated', 'success')
        return redirect(url_for('profile'))
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.email.data = current_user.email    
    image_file = url_for('static', filename='profile_pics/' + current_user.image_file)
    return render_template('profile.html', title='Profile', image_file=image_file, form=form)
    

@app.route("/book/new", methods=['GET', 'POST'])
@login_required
def new_book():    
    form = BookForm()
    if form.validate_on_submit():                            
        book = Book(title=form.title.data, content=form.content.data, author=current_user)      
        db.session.add(book)  
        db.session.commit()
        flash('Your book has been posted', 'success')
        return redirect(url_for('home'))
    return render_template('create_book.html', title='new Book', form=form, legend='New Book')
    
@app.route("/book/<int:book_id>")
def book(book_id):
    book = Book.query.get_or_404(book_id)
    return render_template('book.html', title=book.title, book=book)


@app.route("/book/<int:book_id>/update", methods=['GET', 'POST'])
@login_required
def update_book(book_id):
    book = Book.query.get_or_404(book_id)
    if book.author != current_user:
        abort(403)
    form = BookForm()
    if form.validate_on_submit():
        book.title = form.title.data
        book.content = form.content.data
        db.session.commit()
        flash('Your book details has been updated!', 'success')
        return redirect(url_for('book', book_id=book.id))
    elif request.method == 'GET':
        form.title.data = book.title
        form.content.data = book.content
    return render_template('create_book.html', title='Update Book', form=form, legend='Update Book')


@app.route("/book/<int:book_id>/delete", methods=['POST'])
@login_required
def delete_book(book_id):
    book = Book.query.get_or_404(book_id)
    if book.author != current_user:
        abort(403)
    db.session.delete(book)
    db.session.commit()
    flash('Your book has been deleted!', 'success')
    return redirect(url_for('home'))











    # books = [
    # {
    #     'title': 'Microeconomics',
    #     'bookowner': 'Wenger B',
    #     'bookPicture': 'default.jpg',
    #     'author': 'Corey Schafer',
    #     'content': 'First post content',
    #     'date_posted': 'April 20, 2018'

    # },
    # {
    #     'title':'Primary English',
    #     'bookowner': 'Wenger B',
    #     'bookPicture': 'default.jpg',
    #     'author': 'Greg Norman',
    #     'content': 'Basic English...',
    #     'date_posted': 'May 20, 2019'},

    # {
    #     'title':'Primary Maths',
    #     'bookowner': 'Wenger B',
    #     'bookPicture': 'default.jpg',
    #     'author': 'Robina Hera',
    #     'content': 'First post content',
    #     'date_posted': 'April 20, 2018'}
    # ]



