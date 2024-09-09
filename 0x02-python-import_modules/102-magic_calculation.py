#!/usr/bin/python3
def magic_calculation(a, b):
    import magic_calculation_102
    if a < b:
        c = magic_calculation_102.add(a, b)
        for m in range(4, 6):
            c = magic_calculation_102.add(c, m)
        return c
    else:
        return magic_calculation_102.sub(a, b)
