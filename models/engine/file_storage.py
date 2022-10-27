#!/usr/bin/python3
"""Definition of the FileStorage class."""
import json

class FileStorage:
    """Class FileStorage that serializes instances to a JSON file and deserializes JSON file to instances
    Args:
        __file_path (str): Path to the JSON file (ex: file.json)
        __objects (dict): Empty but will store all objects by <class name>.id

    Methods:
        all(self): returns the dictionary __objects
        new(self, obj): sets in __objects the obj with key <obj class name>.id
        save(self): serializes __objects to the JSON file (path: __file_path)
        reload(self): deserializes the JSON file to __objects
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects
        
        Args:
            self (FileStorage): The current instance
        """
        return self.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id
        
        Args:
            self (FileStorage): The current instance
            obj (any): Any object
        """
        self.__objects["{obj.__class__.__name__}.{obj.id}"]=obj

    def save(self):
        """serializes __objects to the JSON file
        
        Args:
            self (FileStorage): The current instance
        """
        objects_copy = self.__objects.copy()
        objects_dict = {
            obj: objects_copy[obj].to_dict() for obj in objects_copy.keys()
        }

        with open(FileStorage.__file_path, "w") as file:
            json.dump(objects_dict, file)

    def reload(self):
        """deserializes the JSON file to __objects

        Args:
            self (FileStorage): The current instance
        """
        try:
            with open(self.__file_path, "r") as file:
                self.__objects = json.load(file)
        except FileNotFoundError:
            return

