#!/usr/bin/python3
""" Flask Application """
from models import AUTH
from api.v1.views import app_views, app_service, app_apis, app_payment
from models.config import Config, validate_email, check_password
from flask import Flask, jsonify, request, render_template
from flask_mail import Mail, Message
from flask_cors import CORS
from datetime import timedelta
from time import time
import secrets
from uuid import uuid4 as uu


app = Flask(__name__, static_folder='./build', static_url_path='/')
app.secret_key = secrets.token_hex(16)
app.config.from_object(Config)
app.url_map.strict_slashes = False
app.permanent_session_lifetime = timedelta(days=90)
cors = CORS(app, resources={r"*": {"origins": "*"}})
app.register_blueprint(app_views)
app.register_blueprint(app_service)
app.register_blueprint(app_apis)
app.register_blueprint(app_payment)
mail = Mail(app)


@app.teardown_appcontext
def close_db(error):
    """ Close Storage """
    AUTH.close()


@app.errorhandler(404)
@app.route('/')
def frond_end(e=None):
    return app.send_static_file('index.html')


@app.route('/forgot_password', methods=['POST'])
def forgot():
    """send email to user with reset link"""
    email = request.get_json().get('email')
    try:
        validate_email(email)
        token = AUTH.forgot_password(email)
        first_name = AUTH.get_user_with(email=email).first_name
        email_body = render_template('forgot.html', token=token,
                                     first_name=first_name)
        msg = Message('Password Reset',
                      recipients=[email],
                      html=email_body)
        mail.send(msg)
    except Exception as e:
        return jsonify({'error': str(e)}), 400
    return jsonify({'Message':
        'check your email to reset your password'}), 200


@app.route('/signup', methods=['POST'], strict_slashes=False)
def test():
    """test"""
    try:
        data = request.get_json()
        validate_email(data['email'])
        check_password(data['password'])
        data['Time'] = time()
        code = str(uu())
        AUTH.add_code(code, data)
        email_body = render_template('active.html', token=code,
                                     first_name=data['first_name'])
        msg = Message('Activate your account',
                      recipients=[data['email']],
                      html=email_body)
        mail.send(msg)
        return jsonify({'Message':
                        'check your email to activate your account'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400


if __name__ == "__main__":
    """ Main Function """
    app.run(host='0.0.0.0', port=5000,
            threaded=True, debug=True)
