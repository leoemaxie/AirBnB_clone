#!/usr/bin/python3
"""
BaseModel Module: Defines all common attributes/methods for other classes.
This class expose necessary functionalities to manage the console program.
"""
from datetime import datetime
from models import storage
import uuid


class BaseModel:
    """
    The base for all other classes in the console.
    """
    def __init__(self, *args, **kwargs):
        """
        Creates a new instance and serializes it as JSON (provided it is not
        from a dictionary representation)

        Instance attribute:
            id (str) - A unique id of all inherited class
            created_at (datetime) - The time an inherited class was created.
            updated_at (datetime) - The time an inherited class was updated.

        kwargs - Necessary for the serialization of objects using __dict__ if
        provided.
        """
        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    value = datetime.fromisoformat(value)
                if key != "__class__":
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def save(self):
        """
        Updates the public instance attribute updated_at with the current
        datetime
        """
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """
        Returns a dictionary containing all keys/values of __dict__ of the
        instance
        """
        dictionary = {}
        for key, value in self.__dict__.items():
            if key == "created_at" or key == "updated_at":
                value = value.isoformat()
            dictionary.update({key: value})
        dictionary["__class__"] = self.__class__.__name__
        return dictionary

    def __str__(self):
        """
        String representation of an instance in the form:
        [<class name>] (<self.id>) <self.__dict__>
        """
        return "[{}] ({}) {}".format(
            self.__class__.__name__,
            self.id,
            self.__dict__
        )
