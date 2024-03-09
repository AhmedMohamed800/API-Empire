#!/usr/bin/python3
""" Index """
from api.v1.views import app_views
from flask import jsonify, abort


@app_views.route('/status', methods=['GET'], strict_slashes=False)
def status():
    """ Status of API """
    return jsonify({"status": "OK"})


@app_views.route('/abort/<int:status_code>', methods=['GET'], strict_slashes=False)
def abort_status(status_code):
    """ Abort with specified status code """
    abort(status_code)
