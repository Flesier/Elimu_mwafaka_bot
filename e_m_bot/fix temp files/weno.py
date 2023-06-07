from flask import Flask, session, request, render_template, redirect, g, flash, url_for
import mysql.connector
from werkzeug.security import generate_password_hash, check_password_hash
import requests
import openai
import json
#import bot
from flask import Flask, session, request,redirect, g, url_for
from flask import render_template

import os
import json
import mysql.connector


app = Flask(__name__)
app.secret_key = os.urandom(26)


# MySQL Connector configuration
tutordb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "elimumwafaka"
)
#print(tutordb)
mycursor = tutordb.cursor()


#app.config['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'] = "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"



with open(r'C:\xampp\htdocs\Elimu_mwafaka_bot\e_m_bot\maths.json', 'r') as json_file:
    topics = json.load(json_file)


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


# Define routes and add functionality
@app.route('/')
def home():
    return 'Welcome to the TutorBot!'

# Function to authenticate and verify user
def authenticate_user(username, password):
    # Perform SQL query to check username and password in the database
    # Replace the placeholders with your database credentials and query logic
    # You can use a library like SQLAlchemy to interact with the database
    # Here's a sample query using raw SQL:
    query = "SELECT username,password FROM students WHERE username = %s AND password = %s"
    mycursor.execute(query, (username, password))
    result = mycursor.fetchall()
    print(result)
    for row in result:
        print("Username:", row[0])
        print("Password:", row[1])
    name = row[0]
    passw = row[1]
    # Replace this with your own logic to check if the user is authenticated
    # and the password matches the one stored in the database
   
    if username == name and password == passw:
        return True
    else:
        return False

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        if authenticate_user(username, password):
            # Create a session for the authenticated user
            session['username'] = username
            return redirect('/dashboard')
        else:
            error = 'Invalid username or password. Please try again.'
            return render_template('login.html', error=error)
    
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
    if 'username' in session:
        username = session['username']

        query = "SELECT * FROM students WHERE username='{}'".format(username)
        print("Username :".format(username))
    
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

        with open(r'C:\xampp\htdocs\Elimu_mwafaka_bot\e_m_bot\maths.json', 'r') as json_file:
            topics = json.load(json_file)
            print(topics)
        #return render_template('dashboard.html', username=username, lessons=lessons, topics=topics)
        return render_template('dashboard.html', username=username, topics=topics, data=data,form=form)
        #return f'Welcome to the dashboard, {username}!'
    else:
        error="No session Set."
        return redirect('/login')
    # Retrieve user-specific information from the database
   # if 'user' in session:
        #username = session['user']
        #cursor = db.cursor()
        #query = "SELECT * FROM students WHERE username = %s"
        #cursor.execute(query, (username,))
        #user = cursor.fetchone()

        #cursor = db.cursor()
        #cursor.execute("SELECT * FROM lessons")
       # lessons = cursor.fetchall()

        username = "john"
        

        

        
        print("this is the data".format(data))
    #else:
        ################################
        #Remember to change this code
        #return redirect('/login')
       #return render_template('dashboard.html', user=user, lessons=lessons, topics=topics)

    

    #Render the template
    return render_template('app.lessons.html', topics=topics, form=form)
    print("this is the data".format(topics))
    
    


            


    
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

#@app.route('/lessons/<lesson_id>')
@app.route('/lessons', methods=['GET', 'POST'])
def lessons(lesson_id=None):
    #cursor = tutordb.cursor()
    #query = "SELECT * FROM lessons WHERE id = %s"
    #cursor.execute(query, (lesson_id,))
    #lesson = cursor.fetchone()

    #param1 = request.args.get('param1')
    #param2 = request.args.get('param2')

    # Use the parameters to retrieve the necessary information
    # ...

   # return f"Param1: {param1}, Param2: {param2}"
    with open(r'C:\xampp\htdocs\Elimu_mwafaka_bot\e_m_bot\maths.json', 'r') as json_file:
        topics = json.load(json_file)
    

     # Check if the user is logged in
    if 'username' in session:
        username = session['username']

        query = "SELECT * FROM students WHERE username='{}'".format(username)
        print("Form :".format(username))
    
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
        return render_template('lessons.html',topics=topics,form=form)
    else:
        error="No session Set."
        return redirect('/login')

@app.route('/lessons/<lesson_id>/complete', methods=['POST'])
def complete_lesson(lesson_id):
    if 'user' in session:
        username = session['user']
        mycursor = tutordb.cursor()
        query = "SELECT * FROM users WHERE username = %s"
        mycursor.execute(query, (username,))
        user = mycursor.fetchone()

        if user:
            query = "UPDATE users SET lesson_progress = %s WHERE username = %s"
            mycursor.execute(query, (lesson_id, username))
            tutordb.commit()

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