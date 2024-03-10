#!/usr/bin/python3
"""
initialize the models package
"""


from models.engine.auth import Auth
AUTH = Auth()
AUTH.reload()