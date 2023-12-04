#!/usr/bin/python3
""" inherits_from function """


def inherits_from(obj, a_class):
    """
    returns True if the object is an instance of a class
    that inherited (directly or indirectly); otherwise False.
    """

    return(issubclass(type(obj), a_class) and type(obj) != a_class)
