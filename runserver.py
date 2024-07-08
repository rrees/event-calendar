import os

from app import app

PORT = os.environ.get("FLASK_RUN_PORT")

app.app.run(port=PORT, debug=True)
