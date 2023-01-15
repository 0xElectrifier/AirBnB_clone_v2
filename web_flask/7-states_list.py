#!/usr/bin/python3
"""Script that sets up a Flask web application,
fetching the data from MySQL database
"""
from flask import Flask, render_template
from models import storage
app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def states_list():
    states = storage.all('State')
    return render_template('7-states_list.html', states=states)


@app.teardown_appcontext
def teardown():
    storage.close()


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000)
