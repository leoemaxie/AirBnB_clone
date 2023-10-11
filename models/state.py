#!/usr/bin/python3
"""
State Module: Manages the state a user is located in.
"""
from .base_model import BaseModel


class State(BaseModel):
    """
    Public class attributes:
        name: str -> The name of the state. 
    """
    name = ""
