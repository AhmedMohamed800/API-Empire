#!/usr/bin/env python3
"""SQLAlqumy Auth module"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship


class Auth(BaseModel, Base):
    """
    This is the Auth class.

    Attributes:
        hashed_key (str): The hashed key for authentication.
        max_req (int): The maximum number of requests allowed.
        used_req (int): The number of requests already used.

    """

    __tablename__ = 'auth'

    hashed_key = Column(String(128), nullable=False)
    max_req = Column(Integer, nullable=False)
    used_req = Column(Integer, nullable=False)

    def __init__(self, *args, **kwargs):
        """initializes Auth object"""
        super().__init__(*args, **kwargs)
