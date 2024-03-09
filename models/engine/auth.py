#!/usr/bin/env python3
""" auth module for DBStorage """
from models.engine.engine import DBStorage
from models.user import User
from bcrypt import hashpw, gensalt


class Auth:
    """ AUTH class """
    def __init__(self):
        """ init """
        self.storage = DBStorage()
    
    def reload(self):
        """ reload """
        self.storage.reload()

    def create_user(self, **kwargs):
        """ create user """
        admins = ['meemoo102039@gmail.com']
        req = ['email', 'password', 'first_name', 'last_name']
        for r in req:
            if r not in kwargs.keys():
                raise ValueError("{} is required".format(r))
        if self.storage.get('User', email=kwargs['email']):
            raise ValueError("User already exists")
        if kwargs['email'] in admins:
            kwargs['role'] = 'admin'
        else:
            kwargs['role'] = 'user'
        kwargs['hashed_password'] =\
            hashpw(kwargs.pop('password').encode(), gensalt())
        self.storage.new(User(**kwargs))
        self.storage.save()
        return True
    
    def get_all_users(self):
        """ get all users """
        return [user.to_dict() for user in self.storage.all(User).values()]
    
    def close(self):
        """ close """
        self.storage.close()