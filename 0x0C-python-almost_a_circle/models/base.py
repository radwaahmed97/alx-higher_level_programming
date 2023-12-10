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
