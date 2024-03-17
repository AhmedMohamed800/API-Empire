import enum
from sqlalchemy import Column, Integer, String, Enum, ForeignKey, Text
from models.base_model import Base, BaseModel
from sqlalchemy.orm import relationship


class RequestHeaders(enum.Enum):
    string = 'string'
    int = 'int'
    float = 'float'
    boolean = 'boolean'
    array = 'array'
    object = 'object'


class Headers(BaseModel, Base):
    __tablename__ = 'headers'

    name = Column(String(255), nullable=False)
    description = Column(Text, nullable=False)
    type = Column(Enum(RequestHeaders), nullable=False)
    endpoint_id = Column(Integer, ForeignKey('endpoint.id'))

    endpoint = relationship("Endpoint")

    def __init__(self, *args, **kwargs):
        """initializes Headers object"""
        super().__init__(*args, **kwargs)
