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
        """initializes Request object"""
        super().__init__(*args, **kwargs)
