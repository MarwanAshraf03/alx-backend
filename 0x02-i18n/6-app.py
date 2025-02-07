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


@app.before_request
def before_request():
    """runs get_user and puts its result in the global variables g"""
    g.user = get_user()


def get_user():
    """gets the login_as id and gets user from users dictionary"""
    user_id = request.args.get("login_as")
    if user_id:
        user_id = int(user_id)
    return users[user_id] if user_id in users.keys() else None


@babel.localeselector
def get_locale():
    """determine the best match with our supported languages"""
    user_locale = get_user()
    header_locale = request.headers.get("locale")
    print(header_locale)
    locale = request.args.get("locale")
    if locale in Config.LANGUAGES:
        return locale
    elif user_locale:
        if user_locale["locale"] in Config.LANGUAGES:
            return user_locale["locale"]
    elif header_locale:
        return header_locale
    elif Config.BABEL_DEFAULT_LOCALE:
        return Config.BABEL_DEFAULT_LOCALE
    return request.accept_languages.best_match(['en', 'fr'])


class Config:
    """a class to configure the babel instance"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)
# babel = Babel(app, locale_selector=get_locale)


@app.route("/")
def hello_world():
    """returns 5-index.html template"""
    return render_template("5-index.html")


if __name__ == "__main__":
    app.run(debug=True)
