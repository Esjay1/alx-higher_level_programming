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
        area(self): returns the area of the square

    Examples:
        >> a = Square(5)
        >> a.area()
        25

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

    @property
    def size(self):
        """getter method for size"""
        return self.__size

    @size.setter
    def size(self, value):
        """setter method for size"""
        if type(value) == int:
            self.__size = value
        else:
            raise TypeError("size must be an integer")
        if value >= 0:
            self.__size = value
        else:
            raise ValueError("size must be >= 0")

    def area(self):
        return (self.__size * self.__size)

    def my_print(self):
        if self.__size == 0:
            print(" ")
        else:
            for i in range(1, (self.__size + 1)):
                for j in range(1, (self.__size + 1)):
                    if j == self.__size:
                        print("#", end="\n")
                    else:
                        print("#", end="")
