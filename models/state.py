#!/usr/bin/python3
""" State Module for HBNB project """
from os import getenv
from models.base_model import BaseModel, Base
from models.city import City
import models
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String 


class State(BaseModel, Base):
    """ State class
        Attributes:
            name: name
            cities: cities
    """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)

    if getenv("HBNB_TYPE_STORAGE") == "db":
        cities = relationship("City", backref="state", cascade="all, delete-orphan")
    else:
        @property
        def cities(self):
           return [city for city in models.storage.all(City).values()
                  if city.state_id == self.id]
