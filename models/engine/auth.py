#!/usr/bin/env python3
""" auth module for DBStorage """
from models.engine.engine import DBStorage
from models.user import User
from bcrypt import hashpw, gensalt, checkpw
from uuid import uuid4 as uu
from time import time


class AuthEngine:
    """
    The AuthEngine class provides authentication\
        functionality for managing users and sessions.

    Attributes:
        __storage (DBStorage): An instance of the DBStorage class for\
            data storage.
        __tokens (dict): A dictionary to store authentication tokens.

    Methods:
        __init__(): Initializes the AuthEngine class.
        reload(): Reloads the data storage.
        add_code(code, data): Adds an authentication code to\
            the tokens dictionary.
        get_code(code): Retrieves the authentication code from the tokens\
            dictionary and creates a user.
        create_user(**kwargs): Creates a new user with the\
            provided user information.
        get_user(**kwargs): Retrieves user information based\
            on the provided session ID or email.
        login(email, password): Authenticates the user with\
            the provided email and password.
        logout(session_id): Logs out the user with the provided session ID.
        update_user(session_id, **kwargs): Updates the user information\
            with the provided session ID and user data.
        create_session(user): Creates a new session for the user.
        forgot_password(email): Generates a reset token for the user\
            with the provided email.
        reset_password(reset_token, new_password): Resets the user's\
            password with the provided reset token and new password.
        get_user_with(**kwargs): Retrieves user information\
            based on the provided criteria.
        get_reqs(session_id): Retrieves the requests made by the user with\
            the provided session ID.
        all_users(): Retrieves information about all users.
        reqs(session_id): Retrieves the remaining request quota\
            for the user with the provided session ID.
        close(): Closes the data storage connection.
    """

    __storage = None
    __tokens = {}

    def __init__(self):
        """ Initializes the AuthEngine class. """
        self.__storage = DBStorage()

    def reload(self):
        """ Reloads the data storage. """
        self.__storage.reload()

    def add_code(self, code, data):
        """ Adds an authentication code to the tokens dictionary. """
        if self.__storage.get('User', email=data['email']):
            raise ValueError("User already exists")
        self.__tokens[code] = data

    def get_code(self, code):
        """ Retrieves the authentication code from the tokens dictionary\
            and creates a user. """
        if code not in self.__tokens.keys():
            raise ValueError("no code found")
        del self.__tokens[code]['Time']
        self.create_user(self.__tokens[code])
        del self.__tokens[code]
        for k, v in self.__tokens.items():
            if v['Time'] < time() - 300:
                del self.__tokens[k]

    def create_user(self, **kwargs):
        """ Creates a new user with the provided user information. """
        admins = ['meemoo102039@gmail.com',
                  'ahmedmoh0107@gmail.com']
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

    def get_user(self, **kwargs):
        """ get all users """
        if 'session_id' in kwargs:
            session_id = kwargs['session_id']
        elif 'email' in kwargs:
            session_id = kwargs['email']
        if not session_id:
            raise ValueError("no session found")
        user = self.__storage.get('User', session_id=session_id)
        if not user:
            raise ValueError("no user found")
        data = {}
        data['first_name'] = user.first_name
        data['last_name'] = user.last_name
        data['created_at'] = user.created_at
        data['email'] = user.email
        data['role'] = user.role
        if user.auth:
            if user.auth.hashed_key:
                data['api_key'] = user.auth.hashed_key
        return data

    def login(self, email, password):
        """ login """
        user = self.__storage.get('User', email=email)
        if not user:
            raise ValueError("no user found")
        if not checkpw(password.encode('utf-8'),
                       user.hashed_password.encode()):
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
                elif k == 'email':
                    continue
                else:
                    setattr(user, k, v)
        self.__storage.save()

    def create_session(self, user):
        """ create session """
        user.session_id = str(uu())
        self.__storage.save()
        return user.session_id

    def forgot_password(self, email):
        """ forgot password """
        if not email:
            raise ValueError("email is required")
        user = self.__storage.get('User', email=email)
        if not user:
            raise ValueError("no user found")
        user.reset_token = str(uu())
        self.__storage.save()
        return user.reset_token

    def reset_password(self, reset_token, new_password):
        """ reset password """
        if not reset_token:
            raise ValueError("reset token is required")
        if not new_password:
            raise ValueError("new password is required")
        user = self.__storage.get('User', reset_token=reset_token)
        if not user:
            raise ValueError("no user found")
        user.hashed_password = hashpw(new_password.encode(), gensalt())
        user.reset_token = None
        self.__storage.save()
        return True

    def get_user_with(self, **kwargs):
        """ get user with """
        user = self.__storage.get('User', **kwargs)
        if not user:
            raise ValueError("no user found")
        return user

    def get_reqs(self, session_id):
        """ get reqs """
        user = self.__storage.get('User', session_id=session_id)
        if not user:
            raise ValueError("no user found")
        reqs = self.__storage.get('Request', user_id=user.id)
        for r in range(len(reqs)):
            if reqs[r].method:
                reqs[r].method = reqs[r].method.value
            reqs[r] = reqs[r].to_dict()
        return reqs

    def all_users(self):
        """ all users """
        users = [user for user in self.__storage.all(User)]
        return users

    def reqs(self, session_id):
        """ reqs """
        if not session_id:
            raise ValueError("no session found")
        user = self.__storage.get('User', session_id=session_id)
        if not user:
            raise ValueError("no user found")
        if not user.auth:
            raise ValueError("no auth KEY found")
        data = {}
        data['used_req'] = user.auth.used_req
        data['max_req'] = user.auth.max_req
        data['available_req'] = data['max_req'] - data['used_req']
        return data

    def close(self):
        """ close """
        self.__storage.close()
