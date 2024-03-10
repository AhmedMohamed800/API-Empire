#!/usr/bin/env python3
""" holds class endpoint"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, ForeignKey, Enum, Text
from sqlalchemy.orm import relationship
from models.requests import RequestMethod



class Endpoint(BaseModel, Base):
    """ This is the Endpoint class. """
    __tablename__ = 'endpoint'

    title = Column(String(255), nullable=False)
    url = Column(String(255), nullable=False)
    method = Column(Enum(RequestMethod), nullable=False)
    description = Column(Text, nullable=False)
    status_code = Column(Integer, nullable=False)
    response_ex = Column(Text, nullable=False)
    category = Column(String(255), nullable=False)
    api_id = Column(Integer, ForeignKey('API.id'))
    
    api = relationship("API")

    def __init__(self, *args, **kwargs):
        """initializes Endpoint object"""
        super().__init__(*args, **kwargs)
