from flask import Flask, request, jsonify

def home():
    return 'Hello, World como esta todo!'

@app.route('/about')
def about():
    return 'About'

if __name__ == '__main__':
    app.run(debug=True)
