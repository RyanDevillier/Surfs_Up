# Importing flask
from flask import Flask

# Creating the Flask instance "ap"
app = Flask(__name__)

# Creating flask route
@app.route('/')
def hello_world():
    return 'Hello world!'






























