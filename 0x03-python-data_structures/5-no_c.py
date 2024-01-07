#!/usr/bin/python3
def no_c(my_string):
    newstring = []
    for char in my_string:
        if (char == 'c'):
            continue
        elif (char == 'C'):
            continue
        else:
            newstring.append(char)
    newstring1 = ''.join(newstring)
    return newstring1
