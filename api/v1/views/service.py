#!/usr/bin/env python3
"""This module contains the API endpoints for managing services."""

from api.v1.views import app_service
from flask import jsonify
from models import SERVICE


@app_service.route('/all', methods=['GET'], strict_slashes=False)
def get_weather():
    """
    Get all services.

    This function retrieves all services from the database.

    Returns:
        tuple: A tuple containing the JSON response and the HTTP status code.
            The JSON response contains all services.
            The HTTP status code indicates success or failure of the request.
    """
    return jsonify(SERVICE.get_all()), 200


@app_service.route('/<service_id>', methods=['GET'], strict_slashes=False)
def get_service(service_id):
    """
    Get service by ID.

    This function retrieves a service from the database\
        based on the provided service ID.

    Args:
        service_id (str): The ID of the service to retrieve.

    Returns:
        tuple: A tuple containing the JSON response and the HTTP status code.
            The JSON response contains the service details if found,\
                or an error message if not found.
            The HTTP status code indicates success or failure of the request.
    """
    try:
        return jsonify(SERVICE.get(service_id)), 200
    except ValueError as e:
        print(str(e))
        return jsonify({"error": str(e)}), 404
