#!/usr/bin/python3
"""
initialize the models package
"""
from models.engine.auth import Auth
from models.engine.service import Service
from models.engine.key import Key
from models.engine.apis import Apis
from models.engine.invoice import Payment

KEY = Key()
AUTH = Auth()
SERVICE = Service()
APIS = Apis()
INV = Payment()
