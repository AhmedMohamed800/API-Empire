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


paypalrestsdk.configure({
  "mode": "sandbox",
  "client_id": "AY2esf1IcUaQdch1hSLQuZOV2XWbRckjwkqbu5ed-AHPEs-_HzS-boXgFqxawiVq6gckaKQNQwAPyKbq",
  "client_secret": "EMoIHG83MLT9m85QuzYflHv7qyNPjObw2HxNvnjlBKJBKfdDMuXBIlYxdc6dcWoZJKTPMRW3fzNIbClQ"
})

@app_payment.route('/create', methods=['POST'], strict_slashes=False)
def create_payment():
    """Create a payment """
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
    """Execute a payment """
    try:
        INV.create_invoice(request.headers['session-id'],
                           request.get_json()['paymentID'],
                           request.get_json()['amount'])
    except ValueError as e:
        return jsonify({"error": str(e)}), 400
    

@app_payment.route('/all', methods=['GET'], strict_slashes=False)
def all_payment():
    """Get all payments """
    try:
        data = INV.get_invoice(request.headers['session-id'])
        return jsonify(data), 200
    except ValueError as e:
        return jsonify({"error": str(e)}), 400
