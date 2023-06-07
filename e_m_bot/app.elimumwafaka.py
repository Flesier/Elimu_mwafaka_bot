from flask import Flask, session, request, render_template, redirect, g, flash, url_for
import mysql.connector
from werkzeug.security import generate_password_hash, check_password_hash
import requests
import openai
import json
#import bot
import os



app = Flask(__name__)
app.secret_key = os.urandom(26)
#app.config['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'] = "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"



# MySQL Connector configuration
tutordb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "elimumwafaka"
)
#print(tutordb)
mycursor = tutordb.cursor()


@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

# Function to establish a MySQL connection
def create_connection():
    connection = mysql.connector.connect(**db_config)
    return connection


# Define your database models and tables using MySQL connector
#class User:
 #   def __init__(self, username, password):
  #      self.username = username
   #     self.password = generate_password_hash(password)

#class Lesson:
 #   pass

# Set your OpenAI API key
#openai.api_key = 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

# Read JSON data
with open(r'C:\xampp\htdocs\Elimu_mwafaka_bot\e_m_bot\maths.json', 'r') as json_file:
    topics = json.load(json_file)

# Define routes and add functionality
@app.route('/')
def home():
    return 'Welcome to the TutorBot!'

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        #print("Hello world")
        username = request.form['username']
        password = request.form['password']

        cursor = tutordb.cursor()
        query = "SELECT * FROM students WHERE username = %s"
        cursor.execute(query, (username,))
        user = cursor.fetchone()

        if user and check_password_hash(user[2], password):
            session['user'] = username
            return redirect('/dashboard')
        else:
            flash('Invalid credentials', 'error')
            return render_template('login.html', error='Invalid username or password')
       
    return render_template('login.html')
    

@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect('/login')







# Route for the user dashboard
@app.route('/dashboard/', methods=['GET', 'POST'])
@app.route('/dashboard/<data>', methods=['GET', 'POST'])
def dashboard(data=None):
    # Check if the user is logged in
    #if 'user_id' not in session:
       # return redirect('/login')

    # Get the user ID from the session
    #user_id = session['user_id']

    # Retrieve user-specific information from the database
    if 'user' in session:
        username = session['user']
        cursor = db.cursor()
        query = "SELECT * FROM students WHERE username = %s"
        cursor.execute(query, (username,))
        user = cursor.fetchone()

        cursor = db.cursor()
        cursor.execute("SELECT * FROM lessons")
        lessons = cursor.fetchall()

        username = "john"
        query = "SELECT * FROM students WHERE username='{}'".format(username)
    
        mycursor.execute(query)
        data = mycursor.fetchall()
        print(data)

        
        
        for y in data:
            print("Hello niggah{}".format(y))
            #loop in the tuple and set the formats.
            (id, username, first_name,last_name,adm,parent,parent_id,parent_phone,paid,last_point,password,current_school,location,progress,classe,*others) = y
            #Get the email in the tuple
            adm = adm
            classe = classe
            print("Code runner : {}".format(adm))
            print("Code runner : {}".format(classe))
            form = ''
            if classe == "1":
                form = "Form 1"
            elif classe == "2":
                form = "Form 2"
            elif classe == "3":
                form = "Form 3"
            elif classe == "4":
                form = "Form 4"
            else:
                form = "Form 1"

        

        return render_template('dashboard.html', user=user, lessons=lessons, topics=topics)
        print("this is the data".format(data))
    else:
        ################################
        #Remember to change this code
        #return redirect('/login')
        return render_template('dashboard.html', user=user, lessons=lessons, topics=topics)

    
    
    
       




@app.route("/tutorbot", methods=["POST"])
def response():
    data = dict(request.json)
    query = data['query']
    result, prompt_id = chat(query)  # Get the response and prompt ID
    return jsonify({"response": result, "prompt_id": prompt_id})  # Return the response and prompt ID
   
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


    


#To run this app, you need to first export the environment of Flask
"""
in Cmd type
>export FLASK_APP=minimalapp.py
>flask run
or
>python -m flask run
 * Running on http://127.0.0.1:5000/
"""

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)