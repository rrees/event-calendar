import os
import logging

import flask

from . import handlers
from . import middleware
from . import redis_utils

from .routes import page_routes
from .auth_password.routes import auth_routes


ENV = os.environ.get("ENV", "PROD")

redis_url = os.environ.get("REDIS_URL", None)

redis = redis_utils.setup_redis(redis_url)

app = flask.Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY", os.urandom(24))


routes = []

routes = routes + page_routes  # + auth_routes

for path, endpoint, handler, methods in routes:
    app.add_url_rule(path, endpoint, handler, methods=methods)

app.before_request(middleware.require_authorisation)


@app.errorhandler(500)
def server_error(e):
    # Log the error and stacktrace.
    app.logger.exception("An error occurred during a request.")
    return "An internal error occurred.", 500
