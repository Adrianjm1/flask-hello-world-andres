from flask import Flask, request, jsonify
import pgeocode

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello, mi pana!'

@app.route('/about')
def about():
    return 'About'

