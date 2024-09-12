#!/usr/bin/python3

def weight_average(my_list=[]):
    if len(my_list) == 0:
        return 0
    total_addition = 0
    div = 0
    for chars in my_list:
        total_addition += chars[0] * chars[1]
        div += chars[-1]
    return total_addition/div
