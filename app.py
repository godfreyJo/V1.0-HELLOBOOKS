from flask import Flask, jsonify, request, url_for, render_template
from flask_classy import FlaskView, route


app = Flask(__name__)

books = [{'Title': 'Microeconomics'}, {'Title':'Primary English'}, {'Title':'Primary Maths'}]
users = [{'Username': 'John','password':'password'},
        {'Username': 'Joel','password':'password'},
        {'Username': 'Joan','password':'password'},
        {'Username': 'Job','password':'password'}
        ]


#Class view for all the User funvtionalities

class UserView(FlaskView):
    
#Function for viewing  all the users
    @app.route('/users', methods=['GET'])
    def allusers():
        return render_template("user.html");
        # return jsonify({'users': users})
    
#Function for username in the list of all usernames   
    @app.route('/users/<string:name>', methods=['GET'])
    def Usersearch(self, name):
        Usearch = [user for user in users if user['Username']== name]
        return jsonify({'user': Usearch[0]})

 #This function below adds a new user inform of dictionary into the existing dictionary   
    @app.route('/users', methods=['POST'])
    def adduser(self, users):
        user = {'Username': request.json['Username'],
           'password': request.json['password']}
        users.append(user)
        return jsonify({'users': users})
 
 #this function updates the existing username dictionary 
    @app.route('/users/<string:name>', methods=['PUT'])
    def UserEdit(self, username):
        Usearch = [user for user in users if user['Username']== name]
        Usearch [0]['name'] = request.json['Username']
        return jsonify({'user': Usearch[0]})
    
    
#Create a class for viewing various books functionalities
class BooksView(FlaskView):
    
    @app.route('/', methods=['GET'])
    def test():
        return jsonify({'message':'trial!'})


    @app.route('/books', methods=['GET'])
    def allbooks(self):
        return jsonify({'books': books})

    

if __name__ == '__main__':
    app.run(debug=True)