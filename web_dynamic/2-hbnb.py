#!/usr/bin/python3
""" Starts a Flash Web Application """
from models import storage
from flask import Flask, render_template, url_for
import uuid

app = Flask(__name__)


@app.teardown_appcontext
def close_db(error):
    """ Remove the current SQLAlchemy Session """
    storage.close()


@app.route('/2-hbnb/', strict_slashes=False)
def hbnb_filters(the_id=None):
    """
    Handles request to custom template with states, cities and amenities!
    """
    state_objs = storage.all('State').values()
    states = dict([state.name, state] for state in state_objs)
    amenities = storage.all('Amenity').values()
    places = storage.all('Places').values()
    users = dict([user.id, "{} {}".format(user.first_name, user.last_name)]
                 for user in storage.all('User').values())
    cache_id = (str(uuid.uuid4()))
    return render_template('2-hbnb.html', states=states, amenities=amenities,
                           places=places, users=users, cache_id=cache_id)

if __name__ == "__main__":
    """ Main Function """
    app.run(host='0.0.0.0', port=5000)
