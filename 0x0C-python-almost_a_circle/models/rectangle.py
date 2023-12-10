#!/usr/bin/python3
"""Rectangle Class"""
from models.base import Base


class Rectangle(Base):
    """defines Rectangle Class model"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """initializing a rectangle"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """setting/getting width of rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        self.__width = value

    @property
    def height(self):
        """setting/getting height of rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        self.__height = value

    @property
    def x(self):
        """setting/getting x cordinates of rectangle"""
        return self.__x

    @x.setter
    def x(self, value):
        self.__x = value

    @property
    def y(self):
        """setting/getting y cordinates of rectangle"""
        return self.__y

    @y.setter
    def y(self, value):
        self.__y = value
