from flask import Flask, request, jsonify
app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello, mi pana!'

@app.route('/about')
def about():
    return 'About'


@app.route('/query_location', methods=['GET'])
def query_location():
    location = request.args.get('location')
    top_k = request.args.get('top_k', default=3, type=int)
    if not location:
        return jsonify({"error": "Location parameter is required"}), 400
    return 'Hello, mi pana crunch!'
