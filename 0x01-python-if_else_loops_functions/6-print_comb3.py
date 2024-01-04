#!/usr/bin/python3
for m in range(10):
    for n in range(m + 1, 10):
        if m == 8:
            if n == 9:
                continue
        else:
            print("{}{}".format(m, n), end=", ")
print('89')
