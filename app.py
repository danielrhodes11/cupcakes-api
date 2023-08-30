"""Flask app for Cupcakes"""

from flask import Flask, request, jsonify, render_template
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Cupcake
import config


app = Flask(__name__)

app.config.from_object(config.prod_config.Config)

# Check if unittest is running and load test_config
if 'unittest' in config.sys.modules.keys():
    app.config.from_object(config.test_config.TestConfig)

# Check if FLASK_ENVIRONMENT is set to development and load dev_config
if config.os.getenv('FLASK_ENVIRONMENT') == 'development':
    app.config.from_object(config.dev_config.DevConfig)

debug = DebugToolbarExtension(app)

connect_db(app)


@app.route('/')
def show_homepage():
    """Show homepage."""

    return render_template("index.html")

############################## API ROUTES #############################


@app.route('/api/cupcakes')
def all_cupcakes():
    """Get data about all cupcakes."""

    cupcakes = [cupcake.serialize() for cupcake in Cupcake.query.all()]
    return jsonify(cupcakes=cupcakes)


@app.route('/api/cupcakes', methods=["POST"])
def create_cupcake():
    """Create a cupcake with flavor, size, rating and image data from the body of the request. Returns JSON of the newly created cupcake."""

    new_cupcake = Cupcake(flavor=request.json["flavor"], size=request.json["size"],
                          rating=request.json["rating"], image=request.json["image"])
    db.session.add(new_cupcake)
    db.session.commit()
    return (jsonify(cupcake=new_cupcake.serialize()), 201)


@app.route('/api/cupcakes/<int:id>')
def get_cupcake(id):
    """Get data about a single cupcake."""

    cupcake = Cupcake.query.get_or_404(id)
    return jsonify(cupcake=cupcake.serialize())


@app.route('/api/cupcakes/<int:id>', methods=["PATCH"])
def update_cupcake(id):
    """Update a cupcake with the id passed in the URL and flavor, size, rating and image data from the body of the request. Returns JSON of the updated cupcake."""

    cupcake = Cupcake.query.get_or_404(id)
    cupcake.flavor = request.json["flavor"]
    cupcake.size = request.json["size"]
    cupcake.rating = request.json["rating"]
    cupcake.image = request.json["image"]
    db.session.commit()
    return jsonify(cupcake=cupcake.serialize())


@app.route('/api/cupcakes/<int:id>', methods=["DELETE"])
def delete_cupcake(id):
    """Delete a cupcake with the id passed in the URL. Returns JSON of the deleted cupcake."""

    cupcake = Cupcake.query.get_or_404(id)
    db.session.delete(cupcake)
    db.session.commit()
    return jsonify(cupcake=cupcake.serialize())
