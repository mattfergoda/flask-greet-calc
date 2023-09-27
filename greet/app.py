from flask import Flask

app = Flask(__name__)

@app.get('/welcome')
def handle_welcome():
    """Handles get requests at /welcome."""
    return "welcome"

@app.get('/welcome/home')
def handle_welcome_home():
    return "welcome home"

@app.get('/welcome/back')
def handle_welcome_back():
    return "welcome back"

