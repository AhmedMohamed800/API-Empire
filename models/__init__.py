#!/usr/bin/python3
"""
initialize the models package
"""
from models.engine.auth import AuthEngine
from models.engine.service import ServiceEngine
from models.engine.key import KeyEngine
from models.engine.apis import ApisEngine
from models.engine.invoice import PaymentEngine

KEY = KeyEngine()
AUTH = AuthEngine()
SERVICE = ServiceEngine()
APIS = ApisEngine()
INV = PaymentEngine()
