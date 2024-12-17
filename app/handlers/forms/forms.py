import flask

from app.repositories import events

from .form_models import EventForm


def add_event():
    form = EventForm(flask.request.form)
    if form.validate():
        events.create(
            form.start_date.data,
            form.end_date.data,
            form.name.data,
            form.url.data,
            form.notes.data,
        )
        return flask.redirect(flask.url_for("home"))

    flask.abort(400, "Invalid form")
