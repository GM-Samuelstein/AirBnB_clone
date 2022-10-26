#!/usr/bin/python3
"""The definition of a class Amenity that inherits from a class BaseModel"""

from models.base_model import BaseModel


class Amenity(BaseModel):
    """A representation of an amenity.

    Attributes:
        name (str) : Name of the amenity.
    """

    name = ""
