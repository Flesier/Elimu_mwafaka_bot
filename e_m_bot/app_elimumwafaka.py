from flask import Flask, session, request, render_template, redirect, flash
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
import requests
import openai


app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key_here'

# Configure the MySQL database
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://username:password@localhost/db_name'
db = SQLAlchemy(app)

# Define your database models and tables using SQLAlchemy
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(100))
    lesson_progress = db.Column(db.Integer, default=0)

    def __init__(self, username, password):
        self.username = username
        self.password = generate_password_hash(password)

class Lesson(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    description = db.Column(db.Text)

# Set your OpenAI API key
openai.api_key = 'YOUR_API_KEY'

# Define routes and add functionality
@app.route('/')
def home():
    return 'Welcome to the TutorBot!'

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        user = User.query.filter_by(username=username).first()

        if user and check_password_hash(user.password, password):
            session['user'] = username
            return redirect('/dashboard')
        else:
            flash('Invalid credentials', 'error')

    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect('/login')

@app.route('/dashboard')
def dashboard():
    if 'user' in session:
        user = User.query.filter_by(username=session['user']).first()
        lessons = Lesson.query.all()
        return render_template('dashboard.html', user=user, lessons=lessons)
    else:
        return redirect('/login')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if User.query.filter_by(username=username).first():
            flash('Username already taken', 'error')
        else:
            new_user = User(username, password)
            db.session.add(new_user)
            db.session.commit()
            flash('Registration successful! You can now log in.', 'success')
            return redirect('/login')

    return render_template('register.html')

@app.route('/lessons/<lesson_id>')
def lesson_detail(lesson_id):
    lesson = Lesson.query.get(lesson_id)
    return render_template('lesson_detail.html', lesson=lesson)

@app.route('/lessons/<lesson_id>/complete', methods=['POST'])
def complete_lesson(lesson_id):
    if 'user' in session:
        user = User.query.filter_by(username=session['user']).first()
        lesson = Lesson.query.get(lesson_id)
        if user and lesson:
            user.lesson_progress = lesson.id
            db.session.commit()
            flash('Lesson completed!', 'success')
        else:
            flash('Invalid lesson or user', 'error')

    return redirect('/dashboard')

# Run the Flask application
if __name__ == '__main__':
    app.run()
