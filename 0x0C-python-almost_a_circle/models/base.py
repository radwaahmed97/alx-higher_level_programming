#!/usr/bin/python3
"""Base model class"""
import csv
import json


class Base:
    """base model"""

    __nb_objects = 0

    def __init__(self, id=None):
        """initializing new Base"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the JSON string representation of list_dictionaries"""
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)
