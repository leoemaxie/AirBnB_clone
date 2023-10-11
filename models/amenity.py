#!/usr/bin/python3
"""
Amenity Module: Manages the amenities around an accommodation. Examples are:
    Wi-Fi
    Swimming Pools
    Fitness Center
    Parking
"""
from .base_model import BaseModel


class Amenity(BaseModel):
    """
    Public class attributes:
        name: str -> The name of the amenity.
    """
    name = ""
