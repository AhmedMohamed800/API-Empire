from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import scoped_session, sessionmaker, configure_mappers
from sqlalchemy.exc import SQLAlchemyError
from models.base_model import Base
from models.api import API
from models.requests import Request
from models.invoice import Invoice
from models.auth import Auth
from models.endpoint import Endpoint
from models.user import User

classes = {"API": API, "Auth": Auth, "Endpoint": Endpoint,
           "User": User, "Request": Request, 'Invoice': Invoice}


class DBStorage:
    """Interacts with the MySQL database"""
    __engine = None
    __session = None

    def __init__(self):
        """Instantiate a DBStorage object"""
        HBNB_MYSQL_USER = 'api_user'
        HBNB_MYSQL_PWD = 'password'
        HBNB_MYSQL_HOST = 'localhost'
        HBNB_MYSQL_DB = 'api_db'
        try:
            self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.
                                          format(HBNB_MYSQL_USER,
                                                 HBNB_MYSQL_PWD,
                                                 HBNB_MYSQL_HOST,
                                                 HBNB_MYSQL_DB),
                                          pool_size=20,
                                          max_overflow=10,
                                          pool_recycle=3600,
                                          connect_args={'connect_timeout': 10})
            self.reload()  # Initialize the session
        except SQLAlchemyError as e:
            # Handle exceptions
            print("Error in DBStorage.__init__:", e)

    def all(self, cls=None, user_id=None):
        """Query on the current database session"""
        try:
            if cls:
                if user_id:
                    return self.__session.query(cls).filter_by(user_id=user_id
                                                               ).all()
                return self.__session.query(cls).all()
            else:
                return [self.__session.query(cls).all()
                        for cls in classes.values()]
        except SQLAlchemyError as e:
            # Handle exceptions
            print("Error in DBStorage.all:", e)
            return []

    def new(self, obj):
        """Add the object to the current database session"""
        try:
            self.__session.add(obj)
            self.save()  # Save changes immediately
        except SQLAlchemyError as e:
            # Handle exceptions
            print("Error in DBStorage.new:", e)

    def save(self):
        """Commit all changes of the current database session"""
        try:
            self.__session.commit()
        except SQLAlchemyError as e:
            # Handle exceptions
            print("Error in DBStorage.save:", e)

    def delete(self, obj=None):
        """Delete from the current database session obj if not None"""
        try:
            if obj is not None:
                self.__session.delete(obj)
                self.save()  # Save changes immediately
        except SQLAlchemyError as e:
            # Handle exceptions
            print("Error in DBStorage.delete:", e)

    def reload(self):
        """Reloads data from the database"""
        try:
            metadata = MetaData()
            metadata.reflect(bind=self.__engine)
            configure_mappers()
            Base.metadata.create_all(self.__engine)
            sess_factory = sessionmaker(
                bind=self.__engine, expire_on_commit=False)
            self.__session = scoped_session(sess_factory)
        except SQLAlchemyError as e:
            # Handle exceptions
            print("Error in DBStorage.reload:", e)

    def close(self):
        """Call remove() method on the private session attribute"""
        try:
            self.__session.remove()
        except SQLAlchemyError as e:
            # Handle exceptions
            print("Error in DBStorage.close:", e)

    def get(self, cls, **kwargs):
        """
        Returns the object based on the class name and its ID, or
        None if not found
        """
        try:
            if cls not in classes.keys():
                return None

            for key in kwargs.keys():
                if key not in classes[cls].__table__.columns.keys():
                    return None
            if 'api_id' in kwargs or 'user_id' in kwargs and cls == 'Request':
                return self.__session.query(classes[cls]
                                            ).filter_by(**kwargs).all()
            return self.__session.query(classes[cls]
                                        ).filter_by(**kwargs).first()
        except SQLAlchemyError as e:
            # Handle exceptions
            print("Error in DBStorage.get:", e)
            return None

    def update(self, cls, **kwargs):
        """ Update the object """
        try:
            self.__session.query(cls.__class__).filter_by(
                email=cls.email).update(kwargs)
            self.save()  # Save changes immediately
        except SQLAlchemyError as e:
            # Handle exceptions
            print("Error in DBStorage.update:", e)

    def count(self, cls=None):
        """
        Count the number of objects in storage
        """
        try:
            all_class = classes.values()
            if not cls:
                count = 0
                for clas in all_class:
                    count += len(self.all(clas))
            else:
                count = len(self.all(cls))
            return count
        except SQLAlchemyError as e:
            # Handle exceptions
            print("Error in DBStorage.count:", e)
            return 0
