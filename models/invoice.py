#!/usr/bin/env python3
""" holds class Invoice"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, DECIMAL, TIMESTAMP, ForeignKey, String
from sqlalchemy.orm import relationship
from models.user import User

class Invoice(BaseModel, Base):
    __tablename__ = 'invoice'

    payment_id = Column(String(255), nullable=False)
    amount = Column(DECIMAL(10, 2), nullable=False)
    created_at = Column(TIMESTAMP, server_default='CURRENT_TIMESTAMP', nullable=False)
    request = Column(Integer, nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)

    user = relationship(User)

    def __init__(self, *args, **kwargs):
        """Initializes Invoice object"""
        super().__init__(*args, **kwargs)
