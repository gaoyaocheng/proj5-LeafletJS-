import flask
from flask import request
from flask import url_for
from flask import jsonify

import json
import logging
import argparse
import sys

from load_poi import Poi
from secrets import Secret

app = flask.Flask(__name__)
import CONFIG
app.secret_key = CONFIG.secret_key

POI=Poi(CONFIG.poi)
SKEY = Secret()

@app.route("/index")
@app.route("/")
def index():
  flask.g.poi = POI.as_list()
  flask.g.mapquestkey = SKEY.get_mapquest_key()
  flask.g.mapboxkey = SKEY.get_mapbox_key()
  print(flask.g.poi)
  return flask.render_template('leaflet.html')



if __name__ == "__main__":
    app.debug = True
    app.logger.setLevel(logging.DEBUG)
    app.run(port=CONFIG.PORT, host="0.0.0.0", ssl_context="adhoc")

