#!/usr/bin/python3
""" BaseGeometry class """


class BaseGeometry:
    """ class with public attribute area """
    def area(self):
        """ raising exception when call """
        raise Exception("area() is not implemented")
