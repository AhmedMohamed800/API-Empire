import datetime
from sqlalchemy import Column, Integer, String, Enum, TIMESTAMP, ForeignKey
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base
from models.auth import Auth

class User(BaseModel, Base):
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
        """initializes User object"""
        super().__init__(*args, **kwargs)
