#!/usr/bin/python3
""" Flask Application """
from models import AUTH
from api.v1.views import app_views
from models.config import Config
from flask import Flask, make_response, jsonify
from flask_mail import Mail, Message
from flask_cors import CORS
from flasgger import Swagger
from datetime import timedelta
import secrets


app = Flask(__name__)
app.secret_key = secrets.token_hex(16)
app.config.from_object(Config)
app.url_map.strict_slashes = False
app.permanent_session_lifetime = timedelta(days=90)
cors = CORS(app, resources={r"/api/v1/*": {"origins": "*"}})
app.register_blueprint(app_views)
mail = Mail(app)


@app.teardown_appcontext
def close_db(error):
    """ Close Storage """
    AUTH.close()


@app.errorhandler(404)
def not_found(error):
    """ 404 Error
    ---
    responses:
      404:
        description: a resource was not found
    """
    return make_response(jsonify({'error': "Not found"}), 404)

app.config['SWAGGER'] = {
    'title': 'API Empire',
    'uiversion': 1
}

Swagger(app)


if __name__ == "__main__":
    """ Main Function """
    app.run(host='0.0.0.0', port=5000,
            threaded=True, debug=True)
