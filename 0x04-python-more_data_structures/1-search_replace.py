#!/usr/bin/python3
def search_replace(my_list, search, replace):
    newlist = [i for i in my_list]
    for i in newlist:
        if i == search:
            newlist[newlist.index(i)] = replace
    return newlist
