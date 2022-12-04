#!/usr/bin/python3
""" Review module for the HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String


class Review(BaseModel, Base):
    """ Review classto store review information """
    __tablename__ = "Review"
    place_id = Column(String)
    user_id = Column(String)
    text = Column(String)

    def __init__(self, *args, **kwargs):
        """Initialises Amenity"""
        super().__init(*args, **kwargs)

