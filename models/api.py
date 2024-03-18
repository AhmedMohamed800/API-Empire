#!/usr/bin/env python3
"""SQLAlqumy API module"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Text


class API(BaseModel, Base):
    """
    This is the API class.

    Attributes:
        title (str): The title of the API.
        description (str): The description of the API.
        category (str): The category of the API.
        image_cover (str): The image cover of the API.
    """

    __tablename__ = 'API'

    title = Column(String(255), nullable=False)
    description = Column(Text, nullable=False)
    category = Column(String(255), nullable=False)
    image_cover = Column(Text, nullable=True)

    def __init__(self, *args, **kwargs):
        """Initializes API object"""
        super().__init__(*args, **kwargs)
