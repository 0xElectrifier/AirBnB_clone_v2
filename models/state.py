#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128),
                  nullable=False)
    # name = ""

    def __init__(self, *args, **kwargs):
        """Initialises Amenity"""
        super().__init__(*args, **kwargs)

