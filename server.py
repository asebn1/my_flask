from flask import Flask

app = Flask(__name__)

@app.route('/')
def default_route():
    return "Hello, Default Route!"

@app.route('/index')
def index():
    return "Hello, World!"

@app.route('/get_name')
def get_name():
    return "My name flask!"

app.run()

