#!/usr/bin/python3
"""
City Module: Manages the city an accommodation is located.
"""
from models.base_model import BaseModel


class City(BaseModel):
    """
    Public class attributes:
        state_id: str -> Defined by [State.id]. The state_id of the state
        a city is located.
        name: str -> The name of the city.
    """
    name = ""
    state_id = ""
