#!/usr/bin/python3
"""
Place Module: Manages the location of various accommodations auctioned by users
in the website.
"""
from .base_model import BaseModel


class Place(BaseModel):
    """
    Public class attributes:
        - name: str -> The name of the place a user is searching for
        an accomodation.
        - city_id: str -> Defined by [City.id]. The city_id of the state a user
        a city is located.
        - user_id: str -> Defined by [User.id]. The user id of the user
        searching for an accomodation.
        - description: str -> Description of a location.
        - number_rooms: integer -> Number of rooms in an accomodation.
        - number_bathrooms: integer -> Number of bathrooms in an accomodation.
        - max_guest: integer -> Maximum number of guests an accomodation
        can take.
        price_by_night: integer -> Price of an accomodation per night.
        - latitude: float -> latitude coordinate of the location of a user.
        - longitude: float -> longitude coordinate of the location of a user.
        - amenity_ids: list<str> -> List of [Amenity.id].
    """
    name = ""
    city_id = ""
    user_id = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
