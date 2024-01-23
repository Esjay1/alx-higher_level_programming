#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    y = 0
    z = 0
    while (y < x):
        try:
            if type(my_list[y]) == int:
                print("{:d}".format(my_list[y]), end='')
                z += 1
        except (ValueError, TypeError):
            pass
        y += 1
    print('')
    return z
