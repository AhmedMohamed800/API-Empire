#!/usr/bin/env python3
from api.v1.views import app_service
from flask import jsonify
from models import SERVICE
import base64


@app_service.route('/all', methods=['GET'], strict_slashes=False)
def get_weather():
    """ Get weather """
    return jsonify(SERVICE.get_all()), 200


@app_service.route('/<service_id>', methods=['GET'], strict_slashes=False)
def get_service(service_id):
    """ Get service """
    try:
        return jsonify(SERVICE.get(service_id)), 200
    except ValueError as e:
        return jsonify({"error": str(e)}), 404


@app_service.route('/endpoints', methods=['GET'], strict_slashes=False)
def get_endpoints():
    """ Get all endpoints """
    return jsonify(SERVICE.get_all_endpoints()), 200
