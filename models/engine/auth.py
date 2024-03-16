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
        data['api_key'] = user.auth.hashed_key if user.auth.hashed_key else None
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
        return reqs

    def all_users(self):
        """ all users """
        users = [user for user in self.__storage.all(User)]
        return users

    def close(self):
        """ close """
        self.__storage.close()
