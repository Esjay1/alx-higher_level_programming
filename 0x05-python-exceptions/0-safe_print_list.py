#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        y = 0
        while (y < x):
            print("{}".format(my_list[y]), end='')
            y += 1
        print("", end='\n')
    except Exception as e:
        print("")
    return y 
