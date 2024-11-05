#!/usr/bin/env python3
"""simple module to render a web page"""
from flask import Flask, render_template
import flask_babel
app = Flask(__name__)
babel = flask_babel.Babel(app)


class Config:
    """a class to configure the babel instance"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)


@app.route("/")
def hello_world() -> str:
    """returns 0-index.html template"""
    return render_template("1-index.html")


if __name__ == "__main__":
    app.run(debug=True)
