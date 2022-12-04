#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Float, Integer, String


class Place(BaseModel):
    """ A place to stay """
    """__tablename__ = "Place"
    city_id = Column(String)
    user_id = Column(String)
    name = Column(String)
    description = Column(String)
    number_rooms = Column(Integer, nullable=False)
    number_bathrooms = Column(Integer, nullable=False)
    max_guest = Column(Integer, nullable=False)
    price_by_night = Column(Integer, nullable=False)
    latitude = Column(Float, nullable=False)
    longitude = Column(Float, nullable=False)
    amenity_ids = []
    """
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []

    def __init__(self, *args, **kwargs):
        """Initialises Amenity"""
        super().__init__(*args, **kwargs)

