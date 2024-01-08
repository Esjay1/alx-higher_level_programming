def max_integer(my_list=[]):
    result = 0
    if len(my_list) == 0:
        return None
    for char in my_list:
        if char > result:
            result = char
    return result
