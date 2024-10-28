from flask import Flask, request, jsonify
app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello, mi pana!'

@app.route('/about')
def about():
    return 'About'


@app.route('/query_location', methods=['GET'])
def home():
    return 'Hello, mi pana crunch!'
