#!/usr/bin/python3
"""This module contains the views for user operations.

The module defines Flask routes for user-related operations such as
retrieving user information, creating new users, updating user information,
and handling user login and logout.

Routes:
    - /user: Endpoint for user operations.
    - /login: Endpoint for user login and logout.
"""
from api.v1.views import app_views
from flask import jsonify, request
from models import AUTH, KEY


@app_views.route('/user', methods=['GET', 'POST', 'PUT'], strict_slashes=False)
def users():
    """
    Endpoint for user operations.

    GET: Retrieves the user information based on the session ID.
    POST: Creates a new user based on the form data.
    PUT: Updates the user information based on the form data.

    Returns:
        - If successful:
            - GET: JSON representation of\
                the user information with status code 200.
            - POST and PUT: Empty JSON response with status code 200.
        - If unsuccessful:
            - JSON response with an error message and status code 400.
        - POST: JSON response with an error message and status code 201.
    """
    if request.method == 'GET':
        try:
            user = AUTH.get_user(session_id=request.headers.get('session-id'))
            return jsonify(user), 200
        except ValueError as e:
            return jsonify({"error": str(e)}), 400
    elif request.method == 'PUT':
        try:
            AUTH.update_user(request.headers.get('session-id'),
                             **request.get_json())
            return jsonify({}), 200
        except ValueError as e:
            return jsonify({"error": str(e)}), 400
    try:
        AUTH.get_code(request.get_json().get('code'))
    except ValueError as e:
        return jsonify({"error": str(e)}), 400
    return jsonify({}), 201


@app_views.route('/login', methods=['POST', 'DELETE'], strict_slashes=False)
def login():
    """Handles the login endpoint.

    This function handles the login endpoint for the API.
    It allows users to log in by providing their email and password.
    The function supports both POST and DELETE methods.

    Returns:
        A JSON response containing the\
            email and a message indicating whether the user
        has successfully logged in or logged out.

    Raises:
        ValueError: If there is an error during the login or logout process.
    """
    if request.method == 'POST':
        try:
            session_id = AUTH.login(request.form.get('email'),
                                    request.form.get('password'))
            return jsonify({"email": request.form.get('email'),
                           "session": session_id}), 200
        except ValueError as e:
            return jsonify({"error": str(e)}), 400
    try:
        AUTH.logout(request.headers.get('session-id'))
        return jsonify({"message": "Successfully logged out"}), 200
    except ValueError as e:
        return jsonify({"error": str(e)}), 400


@app_views.route('/reset', methods=['POST'], strict_slashes=False)
def reset():
    """Handles the reset endpoint.

    This function handles the reset endpoint for the API.
    It allows users to reset their password by providing their email and
    a new password.

    Returns:
        A JSON response containing the email and a message indicating\
            whether the password has been successfully reset.

    Raises:
        ValueError: If there is an error during the password reset process.
    """
    password = request.get_json().get('password')
    token = request.headers.get('reset-token')
    try:
        AUTH.reset_password(token, password)
        return jsonify({"message": "Password reset successfully"}), 200
    except ValueError as e:
        return jsonify({"error": str(e)}), 400


@app_views.route('/get_key', methods=['POST'], strict_slashes=False)
def get_key():
    """Handles the get_key endpoint.

    This function handles the get_key endpoint for the API.
    It allows users to get their API key.

    Returns:
        A JSON response containing the email and the API key.

    Raises:
        ValueError: If there is an error during the API key retrieval process.
    """
    try:
        key = KEY.create_key(request.headers.get('session-id'))
        return jsonify({"message": "API key created successfully",
                        "key": key}), 201
    except ValueError as e:
        return jsonify({"error": str(e)}), 400


@app_views.route('/get_reqs', methods=['GET'], strict_slashes=False)
def get_reqs():
    """Handles the get_reqs endpoint."""
    try:
        return jsonify(AUTH.get_reqs
                       (request.headers
                        .get('session-id'))), 200
    except ValueError as e:
        return jsonify({"error": str(e)}), 400


@app_views.route('/reqs', methods=['GET'], strict_slashes=False)
def reqs():
    """Handles the reqs endpoint.

    This function is responsible for handling the GET requests to the\
        '/reqs' endpoint.
    It retrieves the session ID from the request headers and passes\
        it to the AUTH.reqs() function.
    The response from AUTH.reqs() is then returned as a JSON object\
        with a status code of 200.
    If any ValueError occurs during the process, it is caught and returned\
        as a JSON object with a status code of 400.

    Returns:
        A JSON response containing the result of the AUTH.reqs()\
            function call or an error message.

    """
    try:
        return jsonify(AUTH.reqs(request.headers.get('session-id'))), 200
    except ValueError as e:
        return jsonify({"error": str(e)}), 400
