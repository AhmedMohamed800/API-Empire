#!/usr/bin/env python3
"""SQLAlqumy Request module"""
import enum
from sqlalchemy import Column, Integer, String, Enum, ForeignKey
from models.base_model import Base, BaseModel
from sqlalchemy.orm import relationship


class RequestMethod(enum.Enum):
    GET = 'GET'
    POST = 'POST'
    PUT = 'PUT'
    DELETE = 'DELETE'


class Request(BaseModel, Base):
    """
    Represents a request made to the API.

    Attributes:
        method (RequestMethod): The HTTP method used for the request.
        ip (str): The IP address of the client making the request.
        status_code (int): The HTTP status code returned by the API.
        path (str): The path of the requested resource.
        date (str): The date and time when the request was made.
        http_version (str): The version of the HTTP protocol used.
        user_id (int): The ID of the user associated with the request.
        user (User): The user associated with the request.

    Methods:
        __init__: Initializes a Request object.

    """

    __tablename__ = 'requests'

    method = Column(Enum(RequestMethod), nullable=False)
    ip = Column(String(255))
    status_code = Column(Integer)
    path = Column(String(255))
    date = Column(String(255))
    http_version = Column(String(255))
    user_id = Column(Integer, ForeignKey('user.id'))

    user = relationship("User")

    def __init__(self, *args, **kwargs):
        """Initializes Request object"""
        super().__init__(*args, **kwargs)
