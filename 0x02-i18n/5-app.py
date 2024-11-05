#!/usr/bin/env python3
"""simple module to render a web page"""
from flask import Flask, render_template, request, g
from flask_babel import Babel
app = Flask(__name__)
babel = Babel(app)
users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}

@app.after_request
def before_request():
    g.user = get_user()


def get_user():
    user_id = request.args.get("login_as")
    return users[user_id] if user_id in users.keys() else None
    # return user_id
    # g.user = users[user_id] if user_id in users.keys() else None

@babel.localeselector
def get_locale():
    """determine the best match with our supported languages"""
    locale = request.args.get("locale")
    if locale in Config.LANGUAGES:
        return locale
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
    return render_template("5-index.html")


if __name__ == "__main__":
    app.run(debug=True)
