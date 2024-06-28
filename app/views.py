"""This module contains the views for the application.

The available views are:
* `home`: The home page of the app, which displays a list of articles
* `about`: A view that displays information about the app
* `contact`: A view that displays contact information for the app
* `hello_there`: A view that says hello to the user with their name
* `get_data`: A view that returns data in JSON format
"""

from datetime import datetime

from flask import Flask, render_template

from . import app


@app.route("/")
def home():
    """The home page of the app, which displays a list of articles

    Returns:
        Any: Home page template
    """
    return render_template("home.html")


@app.route("/about/")
def about():
    """A view that displays information about the app

    Returns:
        Any: About page template
    """
    return render_template("about.html")


@app.route("/contact/")
def contact():
    """A view that displays contact information for the app

    Returns:
        Any: Contact page template
    """
    return render_template("contact.html")


@app.route("/hello/")
@app.route("/hello/<name>")
def hello_there(name=None):
    """A view that says hello to the user with their name

    Args:
        name (str, optional): Name of the user to say hello to. Defaults to None.

    Returns:
        Any: Hello page template
    """
    return render_template("hello_there.html", name=name, date=datetime.now())


@app.route("/api/data")
def get_data():
    """A view that returns data in JSON format

    Returns:
        Any: API data page template
    """
    return app.send_static_file("data.json")
