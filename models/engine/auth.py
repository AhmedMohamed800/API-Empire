#!/usr/bin/env python3
""" auth module for DBStorage """
from models.engine.engine import DBStorage
from models.user import User
from bcrypt import hashpw, gensalt, checkpw
from uuid import uuid4 as uu


class Auth:
    """ AUTH class """
    __storage = None
    def __init__(self):
        """ init """
        self.__storage = DBStorage()
    
    def reload(self):
        """ reload """
        self.__storage.reload()

    def create_user(self, **kwargs):
        """ create user """
        admins = ['meemoo102039@gmail.com']
        req = ['email', 'password', 'first_name', 'last_name']
        for r in req:
            if r not in kwargs.keys():
                raise ValueError("{} is required".format(r))
        if self.__storage.get('User', email=kwargs['email']):
            raise ValueError("User already exists")
        if kwargs['email'] in admins:
            kwargs['role'] = 'admin'
        else:
            kwargs['role'] = 'user'
        kwargs['hashed_password'] =\
            hashpw(kwargs.pop('password').encode(), gensalt())
        self.__storage.new(User(**kwargs))
        self.__storage.save()
        return True
    
    def get_user(self, session_id):
        """ get all users """
        if not session_id:
            raise ValueError("no session found")
        user = self.__storage.get('User', session_id=session_id)
        if not user:
            raise ValueError("no user found")
        del user.hashed_password
        del user.session_id
        del user.id
        return user
    
    def login(self, email, password):
        """ login """
        user = self.__storage.get('User', email=email)
        if not user:
            raise ValueError("no user found")
        if not checkpw(password.encode('utf-8'), user.hashed_password.encode()):
            raise ValueError("invalid password")
        return self.create_session(user)
    
    def logout(self, session_id):
        """ logout """
        if not session_id:
            raise ValueError("no session found")
        user = self.__storage.get('User', session_id=session_id)
        if not user:
            raise ValueError("no user found")
        self.__storage.update(user, session_id=None)
        self.__storage.save()
    
    def update_user(self, session_id, **kwargs):
        """ update user """
        if not session_id:
            raise ValueError("no session found")
        user = self.__storage.get('User', session_id=session_id)
        if not user:
            raise ValueError("no user found")
        for k, v in kwargs.items():
            if k in ['email', 'password', 'first_name', 'last_name']:
                if k == 'password':
                    v = hashpw(v.encode(), gensalt())
                    setattr(user, 'hashed_password', v)
                else:
                    setattr(user, k, v)
        self.__storage.save()

    def create_session(self, user):
        """ create session """
        user.session_id = str(uu())
        self.__storage.save()
        return user.session_id

    def close(self):
        """ close """
        self.__storage.close()
