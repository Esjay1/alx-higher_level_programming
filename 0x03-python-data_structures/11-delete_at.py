#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    newlist = []
    if idx < 0:
        return my_list
    if idx >= len(my_list):
        return my_list
    for char in my_list:
        if my_list.index(char) == idx:
            continue
        if my_list.index(char) != idx:
            newlist.append(char)
    del my_list[idx]
    return newlist
