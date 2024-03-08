#!/usr/bin/env python3
""" This is the API auth module. """
from .engine import Engine

class Authentication:
    """ auth class for the API. """
    def __init__(self):
        """ This is the constructor for the Authentication class."""
        self.__engine = Engine()
    
    def add_user(self, email, password, first_name, last_name):
        """ This method adds a user to the database. """
        return self.__engine.add_user(email, password, first_name, last_name)
    
    def get_all_users(self):
        """ This method gets all users from the database. """
        return self.__engine.get_all_users()