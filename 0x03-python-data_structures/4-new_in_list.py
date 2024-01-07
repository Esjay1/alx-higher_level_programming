#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if idx < 0:
        return my_list
    elif idx >= len(my_list):
        return my_list
    else:
        newlist = []
        for i in my_list:
            newlist.append(i)
        newlist[idx] = element
        return newlist
