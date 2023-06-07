from flask import Flask, session, request,redirect, g
from flask import render_template
#import connection
import os
from flask_mysql import MySQL

app = Flask(__name__)
#app.secret_key = os.random(26)

# MySQL configurations
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'kenyafo_beast'

mysql = MySQL(app)


@app.route('/', methods=['GET', 'POST'])
def login():
    #if request.method == 'POST':
        #session.pop('user', None)  #drop the session before any ativity.
        
    return "Hello world!"

#@app.route('/dashboard/')

#@app.route('/dashboard/<email>', methods=['GET', 'POST'])
#def dashboard(email=None):
 #   return render_template("app.dashboard.html", email=email) 

@app.route('/dashboard')
def dashboard():
    if 'username' not in session:
        return redirect('/login')
    else:
        session['username'] = user['username']
        return redirect('/dashboard')

    username = session['username']
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM affiliateuser WHERE username = %s", (username,))
    data = cursor.fetchall()
    cursor.close()

    return render_template('app.dashboard.html', data=data)
    

    


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






    #----------------------------------------Second Testing COde--------------------------------------------#
    from flask import Flask, session, request,redirect, g
from flask import render_template
import os
import mysql.connector

app = Flask(__name__)
app.secret_key = "your_secret_key"

# MySQL Connector configuration
tutordb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "kenyafo_beast"
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


# Route for the user dashboard
@app.route('/dashboard/<data>', methods=['GET', 'POST'])
def dashboard(data=None):
    # Check if the user is logged in
    #if 'user_id' not in session:
       # return redirect('/login')

    # Get the user ID from the session
    #user_id = session['user_id']

    # Retrieve user-specific information from the database
    #connection = create_connection()
    #cursor = connection.cursor()
    user_email = 'kleekmoses@gmail.com'
    query = "SELECT * FROM affiliateuser WHERE email='{}'".format(user_email)
    #cursor.execute(query)
    #data = cursor.fetchall()
    #sql = "SELECT * FROM affiliateuser WHERE username ='Phill'"
    mycursor.execute(query)
    data = mycursor.fetchall()
    print(data)
    
    for y in data:
        print("Hello niggah{}".format(y))
        #loop in the tuple and set the formats.
        (Id, username, password, date, fname, address,email,referedby,ipaddress,*others) = y
        #Get the email in the tuple
        email = email
        print("Code runner : {}".format(email))

    # Close the database connection
    #cursor.close()
    #connection.close()
    print(data)

    return render_template('app.dashboard.html', data=data)
    print("this is the data".format(data))


    


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