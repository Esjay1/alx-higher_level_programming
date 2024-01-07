#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for char in matrix:
        print('{}'.format((' '.join(map(str, char)))))
