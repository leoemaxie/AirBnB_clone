#!/usr/bin/python3
"""
Review Module: Manages the reviews posted by users.
"""
from .base_model import BaseModel


class Review(BaseModel):
    """
    Public class attributes:
        user_id: str -> Defined by [User.id]. The user id of the user
        submitting a review. 
        place_id: str -> Defined by [Place.id]. The location id of the user
        submitting a review.
        text: str -> The review posted by a user. 
    """
    user_id = ""
    place_id = ""
    text = ""
