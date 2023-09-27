# Put your app in here.
from flask import Flask, request
from operations import add, sub, mult, div

app = Flask(__name__)

@app.get('/add')
def handle_add():
    """Handle get requests to the /add endpoint"""
    return str(add(float(request.args['a']), float(request.args['b'])))

@app.get('/sub')
def handle_sub():
    """Handle get requests to the /sub endpoint"""
    return str(sub(float(request.args['a']), float(request.args['b'])))

@app.get('/mult')
def handle_mult():
    """Handle get requests to the /mult endpoint"""
    return str(mult(float(request.args['a']), float(request.args['b'])))

@app.get('/div')
def handle_div():
    """Handle get requests to the /div endpoint"""
    return str(div(float(request.args['a']), float(request.args['b'])))

