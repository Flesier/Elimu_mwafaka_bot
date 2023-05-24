from flask import Flask, session, request, render_template, redirect, flash
import mysql.connector
from werkzeug.security import generate_password_hash, check_password_hash
import requests
import openai
import json

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key_here'

# Configure the MySQL database
db = mysql.connector.connect(
    host='localhost',
    user='username',
    password='password',
    database='db_name'
)

# Define your database models and tables using MySQL connector
class User:
    def __init__(self, username, password):
        self.username = username
        self.password = generate_password_hash(password)

class Lesson:
    pass

# Set your OpenAI API key
openai.api_key = 'YOUR_API_KEY'

# Read JSON data
with open('maths.json', 'r') as json_file:
    topics = json.load(json_file)

# Define routes and add functionality
@app.route('/')
def home():
    return 'Welcome to the TutorBot!'

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        cursor = db.cursor()
        query = "SELECT * FROM users WHERE username = %s"
        cursor.execute(query, (username,))
        user = cursor.fetchone()

        if user and check_password_hash(user[2], password):
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
        username = session['user']
        cursor = db.cursor()
        query = "SELECT * FROM users WHERE username = %s"
        cursor.execute(query, (username,))
        user = cursor.fetchone()

        cursor = db.cursor()
        cursor.execute("SELECT * FROM lessons")
        lessons = cursor.fetchall()

        return render_template('dashboard.html', user=user, lessons=lessons, topics=topics)
    else:
        return redirect('/login')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        cursor = db.cursor()
        query = "SELECT * FROM users WHERE username = %s"
        cursor.execute(query, (username,))
        user = cursor.fetchone()

        if user:
            flash('Username already taken', 'error')
        else:
            hashed_password = generate_password_hash(password)
            query = "INSERT INTO users (username, password) VALUES (%s, %s)"
            cursor.execute(query, (username, hashed_password))
            db.commit()

            flash('Registration successful! You can now log in.', 'success')
            return redirect('/login')

    return render_template('register.html')

@app.route('/lessons/<lesson_id>')
def lesson_detail(lesson_id):
    cursor = db.cursor()
    query = "SELECT * FROM lessons WHERE id = %s"
    cursor.execute(query, (lesson_id,))
    lesson = cursor.fetchone()

    return render_template('lesson_detail.html', lesson=lesson)

@app.route('/lessons/<lesson_id>/complete', methods=['POST'])
def complete_lesson(lesson_id):
    if 'user' in session:
        username = session['user']
        cursor = db.cursor()
        query = "SELECT * FROM users WHERE username = %s"
        cursor.execute(query, (username,))
        user = cursor.fetchone()

        if user:
            query = "UPDATE users SET lesson_progress = %s WHERE username = %s"
            cursor.execute(query, (lesson_id, username))
            db.commit()

            flash('Lesson completed!', 'success')
        else:
            flash('Invalid lesson or user', 'error')

    return redirect('/dashboard')

# Run the Flask application
if __name__ == '__main__':
    app.run()
