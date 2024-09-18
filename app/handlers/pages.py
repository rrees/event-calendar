import flask

from app.repositories import events as events_repository


def front_page():
    return flask.render_template("index.html")


def home_page():
    events_repository.all()
    return flask.render_template("home.html", events=events_repository.all())
