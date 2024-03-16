#!/usr/bin/python3
"""
Contains the class DBStorage
"""

import models
from models.base_model import Base
from models.api import API
from models.requests import Request
from models.auth import Auth
from models.endpoint import Endpoint
from models.headers import Headers
from models.user import User
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

classes = {"API": API, "Auth": Auth, "Endpoint": Endpoint, "Headers": Headers,
           "User": User, "Request": Request}


class DBStorage:
    """interaacts with the MySQL database"""
    __engine = None
    __session = None

    def __init__(self):
        """Instantiate a DBStorage object"""
        HBNB_MYSQL_USER = 'api_user'
        HBNB_MYSQL_PWD = 'password'
        HBNB_MYSQL_HOST = 'localhost'
        HBNB_MYSQL_DB = 'api_db'
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.
                                      format(HBNB_MYSQL_USER,
                                             HBNB_MYSQL_PWD,
                                             HBNB_MYSQL_HOST,
                                             HBNB_MYSQL_DB),
                                      pool_size=20,
                                      max_overflow=10,
                                      pool_recycle=3600,
                                      connect_args={'connect_timeout': 10})

    def all(self, cls=None):
        """query on the current database session"""
        new_dict = {}
        for clss in classes:
            if cls is None or cls is classes[clss] or cls is clss:
                objs = self.__session.query(classes[clss]).all()
                return objs

    def new(self, obj):
        """add the object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """commit all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete from the current database session obj if not None"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """reloads data from the database"""
        Base.metadata.create_all(self.__engine)
        sess_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        self.__session = scoped_session(sess_factory)

    def close(self):
        """call remove() method on the private session attribute"""
        self.__session.remove()

    def get(self, cls, **kwargs):
        """
        Returns the object based on the class name and its ID, or
        None if not found
        """
        if cls not in classes.keys():
            return None

        for key in kwargs.keys():
            if key not in classes[cls].__table__.columns.keys():
                return None
        if 'api_id' in kwargs or\
            'user_id' in kwargs and cls == 'Request':
            return self.__session.query(classes[cls]).filter_by(**kwargs).all()
        return self.__session.query(classes[cls])\
            .filter_by(**kwargs).first()

    def update(self, cls, **kwargs):
        """ update the object """
        self.__session.query(cls.__class__)\
            .filter_by(email=cls.email).update(kwargs)

    def count(self, cls=None):
        """
        count the number of objects in storage
        """
        all_class = classes.values()

        if not cls:
            count = 0
            for clas in all_class:
                count += len(models.storage.all(clas).values())
        else:
            count = len(models.storage.all(cls).values())

        return count
