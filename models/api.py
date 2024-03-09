#!/usr/bin/env python3
""" holds class API"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Text, VARBINARY


class API(BaseModel, Base):
    """ This is the API class. """
    __tablename__ = 'API'
    
    title = Column(String(255), nullable=False)
    description = Column(Text, nullable=False)
    image_cover = Column(VARBINARY(255), nullable=True)
    category = Column(String(255), nullable=False)
    
    def __init__(self, *args, **kwargs):
        """initializes API object"""
        super().__init__(*args, **kwargs)
