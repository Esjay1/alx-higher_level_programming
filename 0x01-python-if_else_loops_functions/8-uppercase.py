#!/usr/bin/python3
def uppercase(stri):
    for i in stri:
        if (i >= 'a') and (i <= 'z'):
            newstring = (chr((ord(i) - 32)))
        else:
            newstring = i
        print('{}'.format(newstring), end="")
    print()
