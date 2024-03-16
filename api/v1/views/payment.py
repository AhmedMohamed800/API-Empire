#!/usr/bin/python3
"""
This module contains the views for the API endpoints.

It includes the following views:
- status: Returns the status of the API.
- abort_status: Aborts the request with a specified status code.
"""
from api.v1.views import app_payment
from flask import jsonify, abort, request
import paypalrestsdk


paypalrestsdk.configure({
  "mode": "sandbox",  # Change this to "live" for production
  "client_id": "Acc2NHlsRMBVgXGafvkkkvd1QFCRV4HOAPRqfysiLrGYRu_lyKTHDcl4aGbe3zyDe7YG9yd9K2jsv0qe",
  "client_secret": "EPX26zVDzTM2-TSaZu2HthOZnFLIGQJJlQpKEus3D1lbW8pT_aH-UABJkk1YyCB0JzkM3CFk8bVUU67i"
})


app_payment.route('/create', methods=['POST'], strict_slashes=False)
def create_payment():
    """Create a payment """
    data = request.get_json()
    payment = paypalrestsdk.Payment({
        "intent": "sale",
        "payer": {
            "payment_method": "paypal"},
        "redirect_urls": {
            "return_url": "http://localhost:5000/payment/execute",
            "cancel_url": "http://localhost:5000/"},
        "transactions": [{
            "item_list": {
                "items": [{
                    "name": "item",
                    "sku": "item",
                    "price": f"{data['price']}",
                    "currency": f"{data['currency']}",
                    "quantity": 1}]},
            "amount": {
                "total": f"{data['price']}",
                "currency": f"{data['currency']}"},
            "description": "This is the payment transaction description."}]})
    if payment.create():
        return jsonify({"id": payment.id}), 201
    else:
        return jsonify({"error": payment.error}), 400


app_payment.route('/execute', methods=['POST'], strict_slashes=False)
def execute_payment():
    """Execute a payment """
    data = request.get_json()
    payment = paypalrestsdk.Payment.find(data['paymentID'])
    if payment.execute({"payer_id": data['payerID']}):
        return jsonify({"id": payment.id}), 200
    else:
        return jsonify({"error": payment.error}), 400