#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for char in matrix:
        if len(char) >= 1:
            for exmp in char:
                if char.index(exmp) != (len(char) - 1):
                    print('{:d}'.format(exmp), end=' ')
                elif char.index(exmp) == (len(char) - 1):
                    print('{:d}'.format(exmp), end='\n')
        elif len(char) == 0:
            print('{}'.format(''.join(char)))
