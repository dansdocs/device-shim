import os
import flask

def attach_flask_routes(flask_object):
    @flask_object.route('/')
    def index():
        return flask.render_template('index.html')

    @flask_object.route('/favicon.ico')
    def favicon():
        return flask.send_from_directory(os.path.join(flask_object.root_path, 'static'), 'favicon.ico', mimetype='image/vnd.microsoft.icon')

