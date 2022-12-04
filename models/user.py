#!/usr/bin/python3
"""This module defines a class User"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String


class User(BaseModel):
    """This class defines a user by various attributes"""

    """
    __tablename__ = "User"
    email = Column(String)
    password = Column(String)
    first_name = Column(String)
    last_name = Column(String)
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        """Initialises Amenity"""
        super().__init(*args, **kwargs)

