"""Models for Cupcake app."""
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

DEFAULT_IMAGE = "https://tinyurl.com/demo-cupcake"


def connect_db(app):
    """Connect to database."""
    db.app = app
    db.init_app(app)
    app.app_context().push()


class Cupcake(db.Model):
    """Cupcake."""

    __tablename__ = 'cupcakes'

    id = db.Column(db.Integer,
                   primary_key=True,
                   autoincrement=True)

    flavor = db.Column(db.Text,
                       nullable=False)

    size = db.Column(db.Text,
                     nullable=False)

    rating = db.Column(db.Float,
                       nullable=False)

    image = db.Column(db.Text,
                      nullable=False,
                      default=DEFAULT_IMAGE)

    def __repr__(self):
        """Show info about cupcake."""

        c = self
        return f"<Cupcake {c.id} {c.flavor} {c.size} {c.rating} {c.image}>"

    def serialize(self):
        """Serialize to dictionary."""

        return {
            "id": self.id,
            "flavor": self.flavor,
            "size": self.size,
            "rating": self.rating,
            "image": self.image if self.image else DEFAULT_IMAGE
        }

# q: i got a key error when i didnt include the image in a post request. why?
# a: because the image is set to default in the model, but not in the post request. so it's not in the request.json. so it's not in the dictionary. so it's not in the serialize method.
# q: how can i fix this?
