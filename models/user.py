#!/usr/bin/python3
"""
BaseModel Module: Defines all common attributes/methods for other classes.
This class expose necessary functionalities to manage the console program.
"""
from datetime import datetime
from . import storage
import uuid


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
        storage.save()

    def to_dict(self):
        """
        Returns a dictionary containing all keys/values of __dict__ of the
        instance
        """
        self.__dict__["__class__"] = self.__class__.__name__
        self.__dict__["created_at"] = self.created_at.isoformat()
        self.__dict__["updated_at"] = self.updated_at.isoformat()
        return self.__dict__

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
