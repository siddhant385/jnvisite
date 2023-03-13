from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import bcrypt
import jwt

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'
app.config['SECRET_KEY'] = 'secret-key'

db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), nullable=False)
    content = db.Column(db.Text, nullable=False)
    author_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    author = db.relationship('User', backref=db.backref('posts', lazy=True))

    def __repr__(self):
        return '<Post %r>' % self.title

@app.route('/signup', methods=['POST'])
def signup():
    data = request.get_json()
    username = data['username']
    email = data['email']
    password = data['password'].encode('utf-8')

    hashed_password = bcrypt.hashpw(password, bcrypt.gensalt())

    user = User(username=username, email=email, password=hashed_password.decode('utf-8'))
    db.session.add(user)
    db.session.commit()

    return jsonify({'message': 'User created successfully'})

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data['username']
    password = data['password'].encode('utf-8')

    user = User.query.filter_by(username=username).first()

    if user and bcrypt.checkpw(password, user.password.encode('utf-8')):
        token = jwt.encode({'user_id': user.id, 'exp': 14400}, app.config['SECRET_KEY'])

        return jsonify({'token': token.decode('utf-8')})

    return jsonify({'error': 'Invalid username or password'})

@app.route('/create-post', methods=['POST'])
def create_post():
    data = request.get_json()
    title = data['title']
    content = data['content']
    token = data['token']

    try:
        decoded = jwt.decode(

    if:
    __name__ == "__main__"
    app.run(debug=True)

    
 
