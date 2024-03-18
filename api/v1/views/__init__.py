#!/usr/bin/python3
""" Blueprint for API """
from flask import Blueprint

app_views = Blueprint('app_views', __name__, url_prefix='/api/v1')
app_service = Blueprint('app_service', __name__, url_prefix='/api/v1/service')
app_apis = Blueprint('app_apis', __name__, url_prefix='/api')
app_payment = Blueprint('app_payment', __name__, url_prefix='/api/v1/payment')

from api.v1.views.payment import *
from api.v1.views.apis import *
from api.v1.views.service import *
from api.v1.views.users import *
from api.v1.views.index import *
