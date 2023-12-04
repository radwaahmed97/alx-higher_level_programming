#!/usr/bin/python3
"""
mylist class
"""


class MyList(list):
    """a subclass of list"""

    def __init__(self):
        """initializing object"""
        super().__init__()

    def print_sorted(self):
        """print sorted list"""
        print(sorted(self))
