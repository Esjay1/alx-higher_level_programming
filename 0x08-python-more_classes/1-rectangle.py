#!/usr/bin/python3
"""A rectangle class"""


class Rectangle:
    """ the rectangle class """
    def __init__(self, width=0, height=0):
        """ instantation of the class"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """getter mtd for width"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter mtd for width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """getter mtd for height"""
        return self.__height

    @height.setter
    def height(self, value):
        """setter mtd for height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
