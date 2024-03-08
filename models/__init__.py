#!/usr/bin/python3
"""
initialize the models package
"""

from os import getenv



from models.engine.engine import DBStorage
storage = DBStorage()
storage.reload()