#!/usr/bin/env python3
from api.v1.views import app_service
from flask import jsonify
from models import SERVICE
import base64


@app_service.route('/all', methods=['GET'], strict_slashes=False)
def get_weather():
    """ Get weather """
    apis = SERVICE.get_all()
    return jsonify({"message": apis}), 200
