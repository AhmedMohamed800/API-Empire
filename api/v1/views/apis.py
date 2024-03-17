#!/usr/bin/env python3
"""apis class module"""
from api.v1.views import app_apis
from flask import request, jsonify
from models import APIS


@app_apis.route('/weather/<function>', methods=['GET'], strict_slashes=False)
@app_apis.route('/weather', methods=['GET'], strict_slashes=False)
def get_endpoints(function=None):
    """ Get all endpoints """
    try:
        response = APIS.weather(function, request)
        return response.json(), response.status_code
    except ValueError as e:
        return jsonify({"Error": str(e)}), 400


@app_apis.route('/currency', methods=['GET'], strict_slashes=False)
def currency():
    """ Get currency """
    print('in the endpoint')
    try:
        answer = APIS.currency(request)
        return answer.json(), answer.status_code
    except ValueError as e:
        return jsonify({"Error": str(e)}), 400
