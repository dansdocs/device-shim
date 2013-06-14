# coding: utf-8
import flask
import routes
import os
import websocket

flask_pages = flask.Flask(__name__)
flask_pages.secret_key = os.urandom(24)
flask_pages.debug = True
routes.attach_flask_routes(flask_pages)

