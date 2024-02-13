#!/usr/bin/python3
"""A rectangle class"""


class Rectangle:
    """This is the definition of the rectangle class"""
    def __init__(self, width=0, height=0):
        """define the parameters"""
        self.__height = height
        self.__width = width

    """property setter for height"""
    @property
    def height(self):
        """height parameter"""
        return self.__height

    """height setter"""
    @height.setter
    def height(self, value):
        """conditions"""
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

    """Property setter for width"""
    @property
    def width(self):
        """width Parameter"""
        return self.__width

    """width setter"""
    @width.setter
    def width(self, value):
        """width setter"""
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value
