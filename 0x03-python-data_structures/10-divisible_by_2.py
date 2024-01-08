#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    resultlist = []
    i = 0
    while i < len(my_list):
        if (my_list[i] % 2) == 0:
            resultlist.append(True)
        if (my_list[i] % 2) != 0:
            resultlist.append(False)
        i = i + 1
    return resultlist
