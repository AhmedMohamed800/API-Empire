#!/usr/bin/env python3
"""apis class module"""
from api.v1.views import app_apis
from flask import request, jsonify
from models import APIS


@app_apis.route('/weather/<function>', methods=['GET'], strict_slashes=False)
@app_apis.route('/weather', methods=['GET'], strict_slashes=False)
def get_endpoints(function=None):
    """ Get all endpoints.

    This function is responsible for retrieving all\
        endpoints related to weather.
    It calls the `APIS.weather` function passing the\
        `function` parameter and the `request` object.
    The response is returned as a JSON object along\
        with the corresponding status code.

    Args:
        function (str, optional): The specific weather function to retrieve.\
            Defaults to None.

    Returns:
        tuple: A tuple containing the JSON response and the status code.

    Raises:
        ValueError: If an error occurs during the retrieval process,\
            a JSON response with the error message is returned.

    """
    try:
        response = APIS.weather(function, request)
        return response.json(), response.status_code
    except ValueError as e:
        return jsonify({"Error": str(e)}), 400


@app_apis.route('/currency', methods=['GET'], strict_slashes=False)
def currency():
    """Get the exchange rate for a currency.

    This endpoint retrieves the exchange rate for a specific currency.\
        It takes no parameters in the request URL.

    Returns:
        A JSON response containing the exchange\
            rate and the corresponding HTTP status code.

    Raises:
        ValueError: If there is an error retrieving the exchange rate.

    """
    try:
        answer = APIS.currency(request)
        return answer.json(), answer.status_code
    except ValueError as e:
        return jsonify({"Error": str(e)}), 400
