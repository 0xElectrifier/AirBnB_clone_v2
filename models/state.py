#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String


class State(BaseModel):
    """ State class """
    __tablename__ = 'State'
    #name = Column(String)
    name = ""

    def __init__(self, *args, **kwargs):
        """Initialises Amenity"""
        super().__init__(*args, **kwargs)

