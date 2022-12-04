#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String


class City(BaseModel, Base):
    """ The city class, contains state ID and name """

    __tablename__ = 'City'
    state_id = Column(String)
    name = Column(String)

    def __init__(self, *args, **kwargs):
        """Initialises Amenity"""
        super().__init(*args, **kwargs)

