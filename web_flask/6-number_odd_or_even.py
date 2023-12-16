#!/usr/bin/python3
"""
Summary
"""
from flask import Flask, abort, render_template


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


@app.route('/python/<text>', strict_slashes=False)
def pythonreturn(text="is cool"):
    """
    python variable return
    """
    if (text):
        newtext = text.replace("_", " ")
        return f"Python {newtext}"
    else:
        return f"Python {text}"


@app.route('/number/<n>', strict_slashes=False)
def nreturn(n):
    """
    n variable return
    """
    try:
        n = int(n)
        return f"{n} is a number"
    except Exception:
        abort(404)


@app.route('/number_template/<n>', strict_slashes=False)
def renderreturn(n):
    """
    render template, n variable return
    """
    try:
        n = int(n)
        return render_template('5-number.html', number=n)
    except Exception:
        abort(404)


@app.route('/number_odd_or_even/<n>', strict_slashes=False)
def oddevenreturn(n):
    """
    render template odd or even shown , n variable return
    """
    try:
        num = int(n)
        if (num % 2) == 0:
            string = f"{num} is even" 
            return render_template('6-number.html', number=string)
        else:
            string = f"{num} is odd"
            return render_template('6-number.html', number=string)
    except Exception:
        abort(404)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)
