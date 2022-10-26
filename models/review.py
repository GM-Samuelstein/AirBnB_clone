#!/usr/bin/python3
"""The definition of a class Review that inherits from BaseModel class."""

from models.base_model import BaseModel


class Review(BaseModel):
    """A representation of the review of a place.

    Attributes:
        place_id (str) : The id of the place.
        user_id (str) : The id of the user.
        text (str) : The review message.
    """

    place_id = ""
    user_id = ""
    text = ""
