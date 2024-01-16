#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    newdict = {}
    for char in a_dictionary:
        newdict[char] = ((a_dictionary[char]) * 2)
    return newdict
