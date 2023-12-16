#!/usr/bin/python3
"""
Summary
"""
from flask import Flask


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    """
    Index return
    """
    return "Hello HBNB!"

@app.route('/hbnb', strict_slashes=False)
def hbnbreturn():
    """
    Index return
    """
    return "HBNB"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)
