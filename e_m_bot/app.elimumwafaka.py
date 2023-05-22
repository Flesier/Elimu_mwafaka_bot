from flask import Flask, session, request, url_call, redirect, g
from Flask import render_template
import os

app.secret_key = os.random(26)



@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session.pop('user', None)  #drop the session before any ativity.
        
    

    


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
    app.run(host="0.0.0.0" port=5000, debug=True)