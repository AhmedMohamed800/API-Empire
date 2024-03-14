#!/usr/bin/python3
"""
initialize the models package
"""


from models.engine.auth import Auth
from models.engine.service import Service
AUTH = Auth()
SERVICE = Service()
AUTH.reload()
SERVICE.reload()