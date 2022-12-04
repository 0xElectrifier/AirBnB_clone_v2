#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel


class Amenity(BaseModel):
    def __init__(self, *args, **kwargs):
        """Initialises Amenity"""
        super().__init(*args, **kwargs)
    name = ""
