import flask

from app.repositories import events as events_repository
from app import models


def front_page():
    return flask.render_template("index.html")


def home_page():
    events_repository.future(model=models.Event)
    return flask.render_template("home.html", events=events_repository.all())
