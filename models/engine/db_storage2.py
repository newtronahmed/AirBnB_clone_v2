#!/usr/bin/python3
""" Mysql Database storage engine """

from sqlalchemy import create_engine
from models.base_model import BaseModel, Base
from models.city import City
from models.place import Place
from models.state import State
from models.user import User
from models.review import Review
from models.amenity import Amenity

class DBStorage():
    """ DB storage class """
    __engine = None
    __session = None

    def __init__(self):
        self.__engine = create_engine("mysql+mysqldb://{}:{}@{}:{}/{}"
                                      .format(getenv("HBNB_MYSQL_USER"),
                                              getenv("HBNB_MYSQL_PWD"),
                                              getenv("HBNB_MYSQL_HOST"),
                                              3306,
                                              getenv("HBNB_MYSQL_DB")),
                                      pool_pre_ping=True)
        if getenv("HBNB_ENV") == "test":
          Base.metadata.drop_all(bind=self.__engine)
    
    def all(self, cls=None):
        if cls:
            return self.__session.query(cls).all()
        else:
            objs = self.__session.query(State).all()
            objs += self.__session.query(City).all()
            objs += self.__session.query(Place).all()
            objs += self.__session.query(User).all()
            objs += self.__session.query(Review).all()
            objs += self.__session.query(Amenity).all()

            dic = {}
            for row in objs:
                key = type(Self).__name__ + "." + obj.id
                dic[key] = obj
            return dic

    def reload(self):
        from models.user import User
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.place import Place
        from models.review import Review
        
        Base.metadata.create_all(self.__engine)
        self.__session = sessionmaker(bind=self.__engine,
                                      expire_on_commit=False)
        Session = scoped_session(self.__session)
        self.__session = Session()
    
