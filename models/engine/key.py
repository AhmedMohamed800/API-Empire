#!/usr/bin/env python3
from models.engine.engine import DBStorage
from models.auth import Auth
from models.engine.auth import AuthEngine as a
from uuid import uuid4


class KeyEngine:
    """A class that represents a key\
        engine for creating and retrieving keys."""

    def __init__(self):
        """Initialize the KeyEngine class."""
        self.__storage = DBStorage()

    def reload(self):
        """Reload the key engine."""
        self.__storage.reload()

    def create_key(self, session_id):
        """Create a new key for the given session ID.

        Args:
            session_id (str): The session ID.

        Returns:
            str: The hashed key.

        Raises:
            ValueError: If no session is found or no user is found.
        """
        if not session_id:
            raise ValueError("No session found")
        user = self.__storage.get('User', session_id=session_id)
        if not user:
            raise ValueError("No user found")
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
        """Get the key for the given session ID.

        Args:
            session_id (str): The session ID.

        Returns:
            str: The hashed key.

        Raises:
            ValueError: If no session is found,\
                no user is found, or no key is found.
        """
        if not session_id:
            raise ValueError("No session found")
        user = self.__storage.get('User', session_id=session_id)
        if not user:
            raise ValueError("No user found")
        if user.auth is None:
            raise ValueError("No key found")
        return user.auth.hashed_key
