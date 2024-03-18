#!/usr/bin/env python3
"""SQLAlqumy Endpoint module"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, ForeignKey, Enum, Text
from sqlalchemy.orm import relationship
from models.requests import RequestMethod


class Endpoint(BaseModel, Base):
    """
    This is the Endpoint class.

    Attributes:
        title (str): The title of the endpoint.
        url (str): The URL of the endpoint.
        method (RequestMethod): The HTTP request method of the endpoint.
        description (str): The description of the endpoint.
        response_ex (str): The example response of the endpoint.
        category (str): The category of the endpoint.
        api_id (int): The foreign key referencing the API object.

    Relationships:
        api (API): The API object associated with the endpoint.
    """

    __tablename__ = 'endpoint'

    title = Column(String(255), nullable=False)
    url = Column(String(255), nullable=False)
    method = Column(Enum(RequestMethod), nullable=False)
    description = Column(Text, nullable=False)
    response_ex = Column(Text, nullable=False)
    category = Column(String(255), nullable=False)
    api_id = Column(Integer, ForeignKey('API.id'))

    api = relationship("API")

    def __init__(self, *args, **kwargs):
        """Initializes Endpoint object"""
        super().__init__(*args, **kwargs)
