#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) <= 0:
        return None
    else:
        result = my_list[0]
        for char in my_list:
            if char >= result:
                result = char
        return result
