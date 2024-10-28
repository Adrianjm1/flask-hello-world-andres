from flask import Flask
app = Flask(__name__)
@app.route('/')

config = {
    "DEBUG": False,          # some Flask specific configs
    "CACHE_TYPE": "SimpleCache",  # Flask-Caching related configs
    "CACHE_DEFAULT_TIMEOUT": 300
}
app.config.from_mapping(config)

def query_location():
    location = request.args.get('location')
    top_k = request.args.get('top_k', default=3, type=int)
    if not location:
        return jsonify({"error": "Location parameter is required"}), 400
    result = nomi.query_location(location, top_k=top_k)
    result_dict = result.to_dict(orient='records')
    return jsonify(result_dict)


def home():
    return 'Hello, mi pana!'
@app.route('/about')
@app.route('/query_location', methods=['GET'])
def about():
    return 'About'
