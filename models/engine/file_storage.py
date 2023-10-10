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
        if not self.__objects:
            return {}
        return {
            key: value.to_dict() for key, value in self.__objects.items()
        }

    def new(self, obj):
        """
        Sets in __objects the obj with key <obj class name>.id
        Args:
            obj: dict - The object to set
        """
        obj_id = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects.update({obj_id: obj})

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)"""
        with open(self.__file_path, 'w') as file:
            json.dump(self.all(), file)

    def reload(self):
        """
        Deserializes the JSON file to __objects only if the JSON file
        (__file_path) exists
        """
        existing_obj = {}
        try:
            with open(self.__file_path, 'r') as file:
                existing_obj = json.load(file)
        except FileNotFoundError:
            pass

        for key, value in existing_obj.items():
            instance = type(value["name"], tuple(value["__class__"]), {key: value})
            if instance and issubclass(instance, BaseModel):
                self.__objects.update({key: instance})
