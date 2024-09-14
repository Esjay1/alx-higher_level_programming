#!/usr/bin/python3
""" magic class implementation"""
import math


class MagicClass:
    """"bytecode implementation class"""
    def __init__(self, radius=0):
        """ magic class with radius as a parameter"""
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """mtd for calculating the area"""
        return (self.__radius ** 2 * math.pi)

    def circumference(self):
        """mtd for calulating the circumference"""
        return (2 * math.pi * self.__radius)
