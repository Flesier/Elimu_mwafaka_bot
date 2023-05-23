from flask import Flask, session, request
from flask_sqlalchemy import SQLAlchemy
import requests
import openai


app = Flask(__name__)

# Configure the MySQL database
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://username:password@localhost/db_name'
db = SQLAlchemy(app)

# Define your database models and tables using SQLAlchemy
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))

# Set your OpenAI API key
openai.api_key = 'YOUR_API_KEY'

# Define routes and add functionality
@app.route('/')
def home():
    return 'Welcome to the TutorBot!'


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session.pop('user', None)  #drop the session before any ativity.


@app.route('/api/data')
def get_data():
    response = requests.get('https://api.example.com/data')
    if response.status_code == 200:
        return response.json()
    else:
        return 'Error: Failed to fetch data'

@app.route('/api/chat/<prompt>')
def chat(prompt):
    response = openai.Completion.create(
        engine='davinci',
        prompt=prompt,
        max_tokens=100,
        n=1,
        stop=None
    )
    return response.choices[0].text.strip()

# Run the Flask application
if __name__ == '__main__':
    app.run()
