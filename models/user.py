#!/usr/bin/python3
"""
User Module: Manages the users in the website application
"""
from .base_model import BaseModel


class User(BaseModel):
    """
    The base for all other classes in the console.
    Public class attributes:
        email: string - empty string
        password: string - empty string
        first_name: string - empty string
        last_name: string - empty string
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
