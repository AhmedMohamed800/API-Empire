#!/usr/bin/python3
"""
This module contains the views for the API endpoints.

It includes the following views:
- status: Returns the status of the API.
- abort_status: Aborts the request with a specified status code.
"""
from api.v1.views import app_views
from flask import jsonify, abort


@app_views.route('/status', methods=['GET'], strict_slashes=False)
def status():
    """
    Returns the status of the API.

    Returns:
        A JSON response containing the status of the API.
    """
    return jsonify({"status": "OK"})


@app_views.route('/abort/<int:status_code>',
                 methods=['GET'], strict_slashes=False)
def abort_status(status_code):
    """
    Aborts the request with a specified status code.

    Args:
        status_code (int): The status code to be used for aborting the request.

    Returns:
        None

    Raises:
        HTTPException: If the specified status code\
            is not a valid HTTP status code.
    """
    abort(status_code)
