from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from data import Books

Books = Books()

app = Flask(__name__)
Bootstrap(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/signup')
def signup():
    return render_template('signup.html')

@app.route('/profile')
def dashboard():
    return render_template('profile.html')

@app.route('/adm-login')
def profile():
    return render_template('admin-login.html')

@app.route('/admin')
def admin():
    return render_template('admin-area.html')

@app.route('/books')
def books():
    return render_template('books.html', books = Books)

@app.route('/books/<string:id>/')
def book(id):
    return render_template('books.html', id=id)


if __name__ == '__main__':
    app.run(debug=True)