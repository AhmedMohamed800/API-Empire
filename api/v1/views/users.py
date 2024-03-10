#!/usr/bin/python3
""" Index """
from api.v1.views import app_views
from flask import jsonify, request
from models import AUTH


@app_views.route('/users', methods=['GET', 'POST'], strict_slashes=False)
def users():
    """ Status of API """
    if request.method == 'GET':
        return jsonify(AUTH.get_all_users())
    try:
        AUTH.create_user(**request.form.to_dict())
    except ValueError as e:
        return jsonify({"error": str(e)}), 400
    return jsonify({}), 201


# @app_views.route('/login', methods=['POST', 'DELETE'], strict_slashes=False)
# def