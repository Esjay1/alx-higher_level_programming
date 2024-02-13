#!/usr/bin/python3
"""A rectangle class"""


class Rectangle:
    """This is the definition of the rectangle class"""

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """define the parameters"""
        self.__height = height
        self.__width = width
        Rectangle.number_of_instances += 1

    """property setter for height"""
    @property
    def height(self):
        """height parameter"""
        return self.__height

    """height setter"""
    @height.setter
    def height(self, value):
        """conditions"""
        if type(value) != int:
            raise TypeError('height must be an integer')
        elif value < 0:
            raise ValueError('height must be >= 0')
        else:
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
        if type(value) != int:
            raise TypeError('width must be an integer')
        elif value < 0:
            raise ValueError('width must be >= 0')
        else:
            self.__width = value

    """Area of the rectangle"""
    def area(self):
        return (self.__width * self.__height)

    """Perimeter of the rectangle"""
    def perimeter(self):
        if self.__width == 0:
            return 0
        elif self.__height == 0:
            return 0
        else:
            return (2 * (self.__width + self.__height))

    """enable string representation of the class using #"""
    def __str__(self):
        res = ""
        if self.__width == 0:
            return ""
        if self.__height == 0:
            return ""
        for y in range(self.__height):
            if y < (self.__height - 1):
                res = res + ('#' * self.__width) + '\n'
            else:
                res = res + ('#' * self.__width)
        return res

    """recreate a new instance of the rectangle"""
    def __repr__(self):
        return (f"Rectangle({self.__width}, {self.__height})")

    """Action to perform when a delete operation is done"""
    def __del__(self):
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
