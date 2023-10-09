#!/usr/bin/python3
"""
FileStorage Module: Defines  attributes/methods for handling the serialization
and deserialization of class instances using JSON.
"""
from datetime import datetime
import json


class FileStorage:
    """
    Serializes instances to a JSON file and deserializes JSON file to instances
    Private class attribute:
        __file_path: string - path to the JSON file (ex: file.json)
        __objects: dictionary - empty but will store all objects by
                   <classname>.id'
                   example: to store a BaseModel object with id=12121212,
                   the key will be BaseModel.12121212
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects"""
        if self.__objects:
            return self.__objects
        return {}

    def new(self, obj):
        """
        Sets in __objects the obj with key <obj class name>.id
        Args:
            obj: dict - The object to set
        """
        self.__objects = obj

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)"""
        if self.__objects:
            with open(self.__file_path, 'w') as file:
                json.dump(self.all(), file)

    def reload(self):
        """
        Deserializes the JSON file to __objects only if the JSON file
        (__file_path) exists
        """
        try:
            with open(self.__file_path, 'r') as file:
                attr = json.load(file)
                attr["created_at"] = datetime.fromisoformat(attr["created_at"])
                attr["updated_at"] = datetime.fromisoformat(attr["updated_at"])
                del attr["__class__"]
                self.__objects = attr
        except FileNotFoundError:
            pass
