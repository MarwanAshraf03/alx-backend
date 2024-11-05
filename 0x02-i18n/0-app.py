#!/usr/bin/env python3
"""simple module to render a web page"""
from flask import Flask, render_template
app = Flask(__name__)


@app.route("/")
def hello_world() -> str:
    """returns 0-index.html template"""
    return render_template("0-index.html")


if __name__ == "__main__":
    app.run(debug=True)
