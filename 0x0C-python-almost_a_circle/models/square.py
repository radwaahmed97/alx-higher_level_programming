#!/usr/bin/python3
"""defines square model"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """represents a square"""
    def __init__(self, size, x=0, y=0, id=None):
        """initializes square"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """getting/setting size of square"""
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def __str__(self):
        """Return the print() and str() representation of a Square."""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y,
                                                 self.width)
