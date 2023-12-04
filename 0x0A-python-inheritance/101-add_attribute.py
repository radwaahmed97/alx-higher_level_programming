#!/usr/bin/python3

"""function that adds a new attribute to object if it’s possible"""


def add_attribute(obj, attrib, value):
    """adds a new attribute to object if it’s possible
    Args:
        obj (any): The object to add an attribute to.
        attrib (str): The name of the attribute added to obj.
        value (any): The value of att.
    Raises:
        TypeError: If the attribute cannot be added.
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, attrib, value)
