#!/usr/bin/env python3
""" auth module for DBStorage """
from models.engine.engine import DBStorage
from models.api import API
from bcrypt import hashpw, gensalt, checkpw
from uuid import uuid4 as uu


class Service:
    """service class"""
    def __init__(self):
        """ init """
        self.__storage = DBStorage()
    
    def reload(self):
        """ reload """
        self.__storage.reload()
    
    def get_all(self):
        """get all services"""
        return [api.to_dict() for api in self.__storage.all(API)]

    def get_weather(self):
        """ get weather """
        return "sunny"