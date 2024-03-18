#!/usr/bin/python3
"""
This module contains the views for the API endpoints.

It includes the following views:
- status: Returns the status of the API.
- abort_status: Aborts the request with a specified status code.
"""
from api.v1.views import app_payment
from flask import jsonify, request
from models import INV
import paypalrestsdk


ID = 'AHPEs-_HzS-boXgFqxawiVq6gckaKQNQwAPyKbq'
SEC = 'lBKJBKfdDMuXBIlYxdc6dcWoZJKTPMRW3fzNIbClQ'


paypalrestsdk.configure({
    "mode": "sandbox",
    "client_id":
        f"AY2esf1IcUaQdch1hSLQuZOV2XWbRckjwkqbu5ed-{ID}",
    "client_secret":
        f"EMoIHG83MLT9m85QuzYflHv7qyNPjObw2HxNvnj{SEC}"
})


@app_payment.route('/create', methods=['POST'], strict_slashes=False)
def create_payment():
    """Create a payment.

    This function creates a payment using the PayPal REST API.
    It expects a JSON payload in the request body
    containing the necessary payment details such as name, SKU,
    price, and currency. The function then constructs
    a PayPal payment object with the provided details and sends a
    request to create the payment.

    If the payment is successfully created,
    the function extracts the execution token from the payment response
    and returns it as a JSON object with a status code of 201.
    If there is an error during the payment creation,
    the function returns a JSON object with the error
    details and a status code of 400.

    Returns:
        A JSON response containing the execution token or error details.
    """
    data = request.get_json()
    payment = paypalrestsdk.Payment({
        "intent": "sale",
        "payer": {
            "payment_method": "paypal"},
        "redirect_urls": {
            "return_url": "http://localhost:5000/api/v1/payment/execute",
            "cancel_url": "http://localhost:5000/api/v1/payment/cancel"},
        "transactions": [{
            "item_list": {
                "items": [{
                    "name": f"{data['name']}",
                    "sku": f"{data['sku']}",
                    "price": f"{data['price']}",
                    "currency": f"{data['currency']}",
                    "quantity": 1}]},
            "amount": {
                "total": f"{data['price']}",
                "currency": f"{data['currency']}"},
            "description": "This is the payment transaction description."}]})
    if payment.create():
        ECToken = payment.links[1].href.split('token=')[1]
        return jsonify({"id": ECToken}), 201
    else:
        return jsonify({"error": payment.error}), 400


@app_payment.route('/execute', methods=['POST'], strict_slashes=False)
def execute_payment():
    """Execute a payment.

    This function is responsible for executing a payment. It creates an invoice
    using the provided session ID,
    payment ID, and amount. If the payment is successful,
    it returns a JSON response with a success message.
    If any error occurs during the payment execution,
    it returns a JSON response with an error message.

    Returns:
        A JSON response with either a success message or an error message.

    """

    try:
        INV.create_invoice(request.headers['session-id'],
                           request.get_json()['paymentID'],
                           request.get_json()['amount'])
        return jsonify({"message": "payment is successfully done"}), 200
    except ValueError as e:
        return jsonify({"error": str(e)}), 400


@app_payment.route('/all', methods=['GET'], strict_slashes=False)
def all_payment():
    """Get all payments.

    This function retrieves all payment data from the invoice\
        based on the session ID provided in the request headers.

    Returns:
        A JSON response containing the payment data if successful,\
            or an error message if an exception occurs.
    """
    try:
        data = INV.get_invoice(request.headers['session-id'])
        return jsonify(data), 200
    except ValueError as e:
        return jsonify({"error": str(e)}), 400
