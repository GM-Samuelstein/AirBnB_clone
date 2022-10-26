#!/usr/bin/python3
"""The definition of a class City that inherits from the class BaseModel"""

from models.base_model import BaseModel


class City(BaseModel):
    """A representation of a city.

    Attributes:
        state_id (str) : The state id.
        name (str) : The name of the state.
    """

    state_id = ""
    name = ""
