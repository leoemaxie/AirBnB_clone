#!/usr/bin/python3
"""
User Module: Manages the users of the website
"""
from models.base_model import BaseModel


class User(BaseModel):
    """
    Public class attributes:
        email: string -> The email address of a user.
        password: string -> The password of a user.
        first_name: string -> The first name of a user.
        last_name: string -> The last name of a user.
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
