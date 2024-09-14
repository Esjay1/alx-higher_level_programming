#!/usr/bin/python3
"""This task creates an empty class"""


class Square():
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

    def __init__(self, size=0, position=(0, 0)):
        """This defines the acceptable size values"""
        self.size = size
        self.position = position

        """Private attribute"""
    @property
    def size(self):
        """mtd for getting size"""
        return self.__size

    @size.setter
    def size(self, value):
        """setter mtd for size"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """getter mtd for position"""
        return self.__position

    @position.setter
    def position(self, value):
        """setter mtd for position"""
        if (not isinstance(value, tuple) or
            len(value) != 2 or
            not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """mtd for calculating the area"""
        return (self.__size * self.__size)

    def my_print(self):
        """mtd that returns the current area calculation"""
        if self.__size == 0:
            print()
            return
        {print() for i in range(0, self.__position[1])}
        for i in range(self.__size):
            {print(" ", end="") for item in range(0, self.__position[0])}
            {print("#", end="") for k in range(0, self.__size)}
            print("")

    def __str__(self):
        """string rep... of the square"""
        if self.__size != 0:
            {print() for i in range(0, self.__position[1])}
        for i in range(0, self.__size):
            {print(" ", end="") for item in range(0, self.__position[0])}
            {print("#", end="") for k in range(0, self.__size)}
            if i != self.__size - 1:
                print()
        return ("")
