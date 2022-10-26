#!/usr/bin/python3
"""The definition of a class Place that inherits from BaseModel class."""

from models.base_model import BaseModel


class Place(BaseModel):
    """A representation of a place.

    Attributes:
        city_id (str) : The id of the city where the place is located.
        user_id (str) : The id of the user.
        name (str) : The name of the place.
        description (str) : The description of the place.
        number_rooms (int) : The number of rooms that the place has.
        number_bathrooms (int) : The number of bathrooms that the place has.
        max_guest (int) : The maximum number of guests that the place can take.
        price_by_night (int) : The price tag of the place per night.
        latitude (float) : The latitude location of the place.
        longitude (float) : The longitude location of the place.
        amenity_ids (list) : A list of the amenities that the place offers.
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
