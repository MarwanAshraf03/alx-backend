#!/usr/bin/env python3
"""simple module to render a web page"""
from flask import Flask, render_template, request
from typing import Union
from flask_babel import Babel
app = Flask(__name__)
babel = Babel(app)


@babel.localeselector
def get_locale():
    """determine the best match with our supported languages"""
    return request.accept_languages.best_match(['en', 'fr'])


class Config:
    """a class to configure the babel instance"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)


@app.route("/")
def hello_world() -> str:
    """returns 2-index.html template"""
    return render_template("3-index.html")


if __name__ == "__main__":
    app.run(debug=True)
