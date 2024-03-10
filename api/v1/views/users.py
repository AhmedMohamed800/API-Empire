#!/usr/bin/python3
""" Index """
from api.v1.views import app_views
from flask import jsonify, request, session, redirect
from flask_mail import Message
from models import AUTH


@app_views.route('/user', methods=['GET', 'POST', 'PUT'], strict_slashes=False)
def users():
    """ Status of API """
    if request.method == 'GET':
        try:
            user = AUTH.get_user(session['session_id'])
            return jsonify(user), 200
        except ValueError as e:
            return jsonify({"error": str(e)}), 400
    elif request.method == 'PUT':
        try:
            AUTH.update_user(session['session_id'], **request.form.to_dict())
            return jsonify({}), 200
        except ValueError as e:
            return jsonify({"error": str(e)}), 400
    try:
        AUTH.create_user(**request.form.to_dict())
    except ValueError as e:
        return jsonify({"error": str(e)}), 400
    return jsonify({}), 201


@app_views.route('/login', methods=['POST', 'DELETE'], strict_slashes=False)
def login():
    """ login endpoint """
    if request.method == 'POST':
        try:
            session['session_id'] = AUTH.login(request.form.get('email'),
                                               request.form.get('password'))
            if request.form.get('remeber_me'):
                session.permanent = True
            return jsonify({"email": request.form.get('email'),
                            "message": "logged in"}), 200
        except ValueError as e:
            return jsonify({"error": str(e)}), 400
    try:
        AUTH.logout(session['session_id'])
        del session['session_id']
    except ValueError as e:
        return jsonify({"error": str(e)}), 400
    return jsonify({"email": request.form.get('email'),
                    "message": "logged out"})

# @app_views.route('/reset_password', methods=['POST'], strict_slashes=False)
# def reset_password():
#     """ reset password """
#     msg = Message('Subject: Test mail',
#                   sender=Config.MAIL_USERNAME,
#                   recipients=['meemoo102039@gmail.com'])
#     msg.body = "This is the email body"
#     try:
#         mail.send(msg)
#         return 'done'
#     except Exception as e:
#         return jsonify({"error": str(e)}), 400
    # try:
    #     AUTH.reset_password(request.form.get('email'))
    #     return jsonify({"email": request.form.get('email'),
    #                     "message": "password reset"}), 200
    # except ValueError as e:
    #     return jsonify({"error": str(e)}), 400
    # return jsonify({}), 200
