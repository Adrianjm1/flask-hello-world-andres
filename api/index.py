from flask import Flask, request, jsonify
import pgeocode
from flask_caching import Cache

config = {
    "DEBUG": False,          
    "CACHE_TYPE": "SimpleCache",  
    "CACHE_DEFAULT_TIMEOUT": 300
}

app = Flask(__name__)
app.config.from_mapping(config)
cache = Cache(app)
nomi = pgeocode.Nominatim('us')

@app.route('/query_location', methods=['GET'])
@cache.cached(response_hit_indication=True)
@cache.memoize()
def query_location():
    location = request.args.get('location')
    top_k = request.args.get('top_k', default=3, type=int)
    if not location:
        return jsonify({"error": "Location parameter is required"}), 400
    result = nomi.query_postal_code(location, top_k=top_k)
    result_dict = result.to_dict(orient='records')
    return jsonify(result_dict)

@app.route('/')
def home():
    return 'Hello, World como esta todo!'

@app.route('/about')
def about():
    return 'About'

if __name__ == '__main__':
    app.run(debug=True)
