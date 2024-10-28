from flask import Flask, request, jsonify
import pgeocode

app = Flask(__name__)

config = {
    "DEBUG": False,          # some Flask specific configs
    "CACHE_TYPE": "SimpleCache",  # Flask-Caching related configs
    "CACHE_DEFAULT_TIMEOUT": 300
}
app.config.from_mapping(config)

@app.route('/')
def home():
    return 'Hello, mi pana!'

@app.route('/about')
def about():
    return 'About'

@app.route('/query_location', methods=['GET'])
def query_location():

    return 'prueba'
