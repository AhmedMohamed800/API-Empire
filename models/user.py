#!/usr/bin/env python3
"""SQLAlqumy User module"""
import datetime
from sqlalchemy import Column, Integer, String, Enum, TIMESTAMP, ForeignKey
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base
from models.auth import Auth


class User(BaseModel, Base):
    """
    This class represents a user in the system.

    Attributes:
        email (str): The email address of the user.
        hashed_password (str): The hashed password of the user.
        first_name (str): The first name of the user.
        last_name (str): The last name of the user.
        created_at (datetime): The timestamp when the user was created.
        session_id (str): The session ID of the user.
        reset_token (str): The reset token of the user.
        role (str): The role of the user. Can be 'admin' or 'user'.
        auth_id (int): The ID of the associated authentication record.

    Relationships:
        auth (Auth): The authentication record associated with the user.
    """

    __tablename__ = 'user'

    email = Column(String(255), unique=True)
    hashed_password = Column(String(255))
    first_name = Column(String(255))
    last_name = Column(String(255))
    created_at = Column(TIMESTAMP, default=datetime.datetime.utcnow)
    session_id = Column(String(255))
    reset_token = Column(String(255))
    role = Column(Enum('admin', 'user'), default='user')
    auth_id = Column(Integer, ForeignKey('auth.id'))

    auth = relationship("Auth")

    def __init__(self, *args, **kwargs):
        """Initializes a new User object."""
        super().__init__(*args, **kwargs)
