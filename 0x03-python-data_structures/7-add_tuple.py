#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    newtuplea = list(tuple_a)
    newtupleb = list(tuple_b)
    if len(newtuplea) == 0:
        newtuplea.append(0)
        newtuplea.append(0)
    if len(newtupleb) == 0:
        newtupleb.append(0)
        newtupleb.append(0)
    if len(newtuplea) < 2:
        newtuplea.append(0)
    if len(newtupleb) < 2:
        newtupleb.append(0)
    resulttuple = [newtuplea[0] + newtupleb[0], newtuplea[1] + newtupleb[1]]
    resulttuple1 = tuple(resulttuple)
    return resulttuple1
