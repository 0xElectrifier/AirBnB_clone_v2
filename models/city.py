#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String


Base = declarative_base()
class City(BaseModel, Base):
    """ The city class, contains state ID and name """

    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        """Initialises Amenity"""
        super().__init(*args, **kwargs)

