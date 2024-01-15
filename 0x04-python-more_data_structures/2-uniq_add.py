#!/usr/bin/python3
def uniq_add(my_list=[]):
    newset = set(my_list)
    listsum = 0
    for char in newset:
        listsum = listsum + char
    return listsum
