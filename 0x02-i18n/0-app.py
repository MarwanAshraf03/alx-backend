#!/usr/bin/python3
"""simple module"""
from flask import Flask, render_template
app = Flask(__name__)


@app.route("/")
def hello_world() -> None:
    """returns 0-index.html template"""
    return render_template("0-index.html")
