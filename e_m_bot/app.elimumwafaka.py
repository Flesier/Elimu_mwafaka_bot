from flask import Flask, session, request,redirect, g, url_for
from flask import render_template
import os
import json
import mysql.connector

app = Flask(__name__)
app.secret_key = "your_secret_key"

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
    
    user_adm = 'john.sim@example.com'
    query = "SELECT * FROM students WHERE adm='{}'".format(user_adm)
   
    mycursor.execute(query)
    data = mycursor.fetchall()
    print(data)

    
    
    for y in data:
        print("Hello niggah{}".format(y))
        #loop in the tuple and set the formats.
        (id, username, first_name,last_name,adm,parent,parent_id,parent_phone,paid,last_point,password,current_school,location,progress,classe,*others) = y
        #Get the email in the tuple
        adm = adm
        print("Code runner : {}".format(adm))

    with open(r'C:\xampp\htdocs\Elimu_mwafaka_bot\e_m_bot\maths.json', 'r') as json_file:
        topics = json.load(json_file)
        # Loop over the data
        for key, value in topics.items():
            print("{}: {}".format(key, value))
            if key == 'Form 1':
                print("This are the topics: {}".format(value))
                Tnames = value

    
    return render_template('app.dashboard.html', data=data, topics=topics)
    print("this is the data".format(data))
       
            

    


            


        
#print("Graetasndbsnsldmnfkjbnkwlmkd{}".format(data))
# Query the subtopics for Form 4
#form4_subtopics = data['Form 4']

# Access individual subtopics
#trigonometry_subtopics = form4_subtopics['Trigonometry']
#calculus_subtopics = form4_subtopics['Calculus']

# Print the subtopics
#print("Trigonometry subtopics:")
#for subtopic in trigonometry_subtopics:
   # print(subtopic)

#print("\nCalculus subtopics:")
#for subtopic in calculus_subtopics:
    #print(subtopic)


    





    






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