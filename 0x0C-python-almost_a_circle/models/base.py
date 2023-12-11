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

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of list_objs to a file"""
        fname = cls.__name__ + ".json"
        with open(fname, "w") as jsonfile:
            if list_objs is None:
                jsonfile.write("[]")
            else:
                listdictionaries = [obj.to_dictionary() for obj in list_objs]
                jsonfile.write(Base.to_json_string(listdictionaries))

    @staticmethod
    def from_json_string(json_string):
        """ returns the list of JSON string representation json_string"""
        if json_string is None or json_string == []:
            return "[]"
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes already set"""
        if dictionary and dictionary != {}:
            if cls.__name__ == "Rectangle":
                n = cls(1, 1)
            else:
                n = cls(1)
            n.update(**dictionary)
            return n
