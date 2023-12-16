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
    HBNH return
    """
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def creturn(text):
    """
    C variable return
    """
    newtext = text.replace("_", " ")
    return f"C {newtext}"


@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def pythonreturn(text="is cool"):
    """
    python variable return
    """
    if text == "":
        text = "is cool"
    newtext = text.replace("_", " ")
    return f"Python {newtext}"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)
