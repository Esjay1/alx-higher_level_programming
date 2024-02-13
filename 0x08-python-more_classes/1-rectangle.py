#!/usr/bin/python3
"""A rectangle class"""


class Rectangle:
    """This is the definition of the rectangle class"""
    def __init__(self, width=0, height=0):
        self.__height = height
        self.__width = width

    """property setter for height"""
    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) != (int or float):
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

    """Property setter for width"""
    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) != (int or float):
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value
