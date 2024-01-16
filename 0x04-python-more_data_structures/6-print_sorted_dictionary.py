#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    sorteddict = sorted(a_dictionary.keys())
    for sort in sorteddict:
        print("{}: {}".format(sort, (a_dictionary[sort]), end='\n'))
