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

    def __init__(self, size=0, position=(0, 0)):
        """This defines the acceptable size values"""
        if type(size) == int:
            self.__size = size
        else:
            raise TypeError("size must be an integer")
        if size >= 0:
            self.__size = size
        else:
            raise ValueError("size must be >= 0")
        self.__position = position

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
        """this method computes the area of the square"""
        return (self.__size * self.__size)

    def my_print(self):
        """this method prints the square with #"""
        if self.__size == 0:
            print(" ")
        else:
            for i in range(self.__position[1]):
                if j == self.__size:
                    print("#", end="\n")
                else:
                    print("#", end="")

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        for item in value:
            if type(item) != int:
                raise TypeError("position must be a tuple of 2 positive \
                        integers")
            else:
                self.__position = value

    def my_print(self):
        if self.__size == 0:
            print(" ")
        else:
            for i in range(self.__position[1]):
                print()
            for j in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)
    
    def __str__(self):
        """return square in string representation"""
        ans = ""
        if self.__size == 0:
            ans = ans + "\n"
        else:
            for i in range(self.__position[1]):
                ans = ans + "\n"
            for j in range(self.__size):
                ans += " " * self.__position[0] + '#' * self.__size + "\n"
        return ans.strip()
