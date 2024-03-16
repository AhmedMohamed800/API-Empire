#!/usr/bin/env python3
from models.engine.engine import DBStorage
from models.auth import Auth
from models.engine.auth import Auth as a
from uuid import uuid4


class Key:
    """key class"""
    def __init__(self):
        """init"""
        self.__storage = DBStorage()

    def reload(self):
        """reload"""
        self.__storage.reload()

    def create_key(self, session_id):
        """create key"""
        if not session_id:
            raise ValueError("no session found")
        user = self.__storage.get('User', session_id=session_id)
        if not user:
            raise ValueError("no user found")
        key = Auth()
        if user.auth_id is None:
            key.max_req = 1000
            key.used_req = 0
        else:
            key.max_req = user.auth.max_req
            key.used_req = user.auth.used_req
            self.__storage.delete(user.auth)
        key.hashed_key = str(uuid4())
        user.auth = key
        self.__storage.new(key)
        self.__storage.save()
        return key.hashed_key

    def get_key(self, session_id):
        """get key"""
        if not session_id:
            raise ValueError("no session found")
        user = self.__storage.get('User', session_id=session_id)
        if not user:
            raise ValueError("no user found")
        if user.auth is None:
            raise ValueError("no key found")
        return user.auth.hashed_key
