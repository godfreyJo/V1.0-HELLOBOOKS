from flask import Flask, render_template, jsonify
from flask_bootstrap import Bootstrap
from data import Books
import uuid
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLALchemy

app.config['SECRET_KEY'] ='secret'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:'

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

@app.route('/book/<string:id>/')
def book(id):
    return render_template('book.html', id=id)

class User(db.Model):
    id = db.Column(db.Interger, primary_key=True)
    public_id = db.Column(db.String(50), unique=True)
    name = db.Column(db.String(50))
    password = db.Column(db.String(80))
    admin = db.Column(db.Boolean

#class Borrow(db.Model):
#    id = db.Column(db.Interger, primary_key=True)
#    complete = db.Column(db.Boolean)
#    user_id  = db.Column(db.Integer)
                      
@app.route('/user', methods=['POST'])
def create_user():
    data = request.get_json()
    hashed_password = generate_password_hash(data['password'], method='sha256')
    new_user = User(public_id=str(uuid.uuid4()), name=data['name'], password=hashed_password, admin=False)
    db.session.add(new_user)
    db.session.commit()

    return jsonify({'message': 'New user created '})
                     
                     
                     
                      )


if __name__ == '__main__':
    app.run(debug=True)