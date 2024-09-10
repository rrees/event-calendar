import os

import flask


def check_credentials(username, password):
    valid_users = os.environ.get("VALID_USERS").split(",")
    return username in valid_users and password == os.environ.get("ADMIN_PASSWORD")


def require_authorisation():
    auth = flask.request.authorization
    if (
        not auth
        or not auth.username
        or not auth.password
        or not check_credentials(auth.username, auth.password)
    ):
        return flask.Response(
            "Please login", 401, {"WWW-Authenticate": 'Basic realm="contact-sport"'}
        )
