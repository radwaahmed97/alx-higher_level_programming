#!/usr/bin/python3
""" BaseGeometry class """


class BaseGeometry:
    """ class with public attribute area """
    def area(self):
        """ raising exception when call """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validating value is an integer greater than 0"""
        if type(value) is not int:
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))
