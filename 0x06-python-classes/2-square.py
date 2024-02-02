#!/usr/bin/python3
"""This task creates an empty class"""


class Square:
    """This class defines what a Square is
    but the task requres me to create an empty
    one for now.

    Attributes:
        size: to be a private attribute

    Methods:
        __init__(self, size): initializes the size attribute

    Examples:
        No example yet

    """
    def __init__(self, size=0):
        """This defines the acceptable size values"""
        if type(size) == int:
            self.__size = size
        else:
            raise TypeError("size must be an integer")
        if size >= 0:
            self.__size = size
        else:
            raise ValueError("size must be >= 0")
