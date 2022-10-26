#!/usr/bin/python3
"""The definition of a class State that inherits from BaseModel class"""

from models.base_model import BaseModel


class State(BaseModel):
    """A representation of a state.

    Attributes:
        name (str) : The name of the state.
    """

    name = ""
