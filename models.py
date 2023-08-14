"""Models for Cupcake app."""
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

DEFAULT_IMAGE = "https://tinyurl.com/demo-cupcake"


def connect_db(app):
    """Connect to database."""
    db.app = app
    db.init_app(app)
    app.app_context().push()
