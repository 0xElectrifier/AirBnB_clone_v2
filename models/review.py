#!/usr/bin/python3
""" Review module for the HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from models import HBNB_TYPE_STORAGE


class Review(BaseModel, Base):
    """ Review classto store review information """
    __tablename__ = "reviews"
    __table_args__ = ({'mysql_default_charset': 'latin1'})

    if HBNB_TYPE_STORAGE == 'db':
        text = Column(String(1024), nullable=False)
        place_id = Column(String(60), ForeignKey('places.id'), nullable=False)
        user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    else:
        place_id = ""
        user_id = ""
        text = ""

    def __init__(self, *args, **kwargs):
        """Initialises Amenity"""
        super().__init__(*args, **kwargs)
