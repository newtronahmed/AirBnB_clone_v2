#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship


class City(BaseModel, Base):
    """ The city class, contains state ID and name
        Attributes:
            name: name of city
            state_id: foreign key
    """
    __tablename__ = "cities"

    name = Column(String(128), nullable=False)
    state_id = Column(String(60), nullable=False, ForeignKey("states.id"))
    places = relationship('Place', back_ref="cities",
                          cascade="all, delete-orphan")
