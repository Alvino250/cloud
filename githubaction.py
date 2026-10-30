from flask import Flask, request
from markupsafe import escape
app = Flask(__name__)

@app.route('/')
def helloWorld():
    return 'Hello, World!'

