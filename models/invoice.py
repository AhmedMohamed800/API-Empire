#!/usr/bin/env python3
"""SQLAlqumy Inovice module"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, DECIMAL, TIMESTAMP, ForeignKey, String
from sqlalchemy.orm import relationship
from models.user import User


class Invoice(BaseModel, Base):
    """
    Represents an invoice.

    Attributes:
        payment_id (str): The ID of the payment associated with the invoice.
        amount (decimal.Decimal): The amount of the invoice.
        created_at (datetime.datetime):\
            The timestamp when the invoice was created.
        request (int): The request ID associated with the invoice.
        user_id (int): The ID of the user associated with the invoice.
        user (User): The user object associated with the invoice.
    """

    __tablename__ = 'invoice'

    payment_id = Column(String(255), nullable=False)
    amount = Column(DECIMAL(10, 2), nullable=False)
    created_at = Column(
        TIMESTAMP, server_default='CURRENT_TIMESTAMP', nullable=False)
    request = Column(Integer, nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)

    user = relationship(User)

    def __init__(self, *args, **kwargs):
        """Initializes Invoice object"""
        super().__init__(*args, **kwargs)
