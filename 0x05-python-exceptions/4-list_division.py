#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):

    try:
        newlist = []
        y = 0
        while y < list_length:
            item1 = my_list_1[y] if (y < len(my_list_1)) else 0
            item2 = my_list_2[y] if (y < len(my_list_2)) else 0
            divresult = item1 / item2
            newlist.append(divresult)
            y = y + 1
    except (TypeError, ValueError):
        print("wrong type")
        newlist.insert(y, 0)
    except ZeroDivisionError:
        print("division by 0")
        newlist.insert(y, 0)
    except IndexError:
        print("out of range")
        newlist.insert(y, 0)
    finally:
        pass
    return (newlist)
