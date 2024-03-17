#!/usr/bin/env python3
from sqlalchemy import Column, Integer, DECIMAL, TIMESTAMP, ForeignKey, String
from sqlalchemy.orm import relationship
from models.base_model import Base, BaseModel
from models.user import User

class Invoice(BaseModel, Base):
    __tablename__ = 'invoice'

    id = Column(Integer, primary_key=True, autoincrement=True)
    payment_id = Column(String(255))
    amount = Column(DECIMAL(10, 2))
    created_at = Column(TIMESTAMP, server_default='CURRENT_TIMESTAMP')
    request = Column(Integer)
    user_id = Column(Integer, ForeignKey('user.id'))

    user = relationship(User)

    def __init__(self, *args, **kwargs):
        """Initializes Invoice object"""
        super().__init__(*args, **kwargs)