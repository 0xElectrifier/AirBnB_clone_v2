#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String


lass City(BaseModel, Base):
    """ The city class, contains state ID and name """

    __tablename__ = 'City'
    state_id = Column(String)
    name = Column(String)

    def __init__(self, *args, **kwargs):
        """Initialises Amenity"""
        super().__init(*args, **kwargs)

