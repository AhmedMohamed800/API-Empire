#!/usr/bin/env python3
""" holds class Auth"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship


class Auth(BaseModel, Base):
    """ This is the Auth class. """
    __tablename__ = 'auth'

    hashed_key = Column(String(128), nullable=False)
    max_req = Column(Integer, nullable=False)
    used_req = Column(Integer, nullable=False)

    user = relationship("User")

    def __init__(self, *args, **kwargs):
        """initializes Auth object"""
        super().__init__(*args, **kwargs)
