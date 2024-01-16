#!/usr/bin/python3
def best_score(a_dictionary):
    test = 0
    if a_dictionary == None:
        return None
    if len(a_dictionary) == 0: 
        return None
    if len(a_dictionary) >= 1:
        for char in a_dictionary:
            if a_dictionary[char] > test:
                test = a_dictionary[char]
        for value in a_dictionary:
            if a_dictionary[value] == test:
                return value
