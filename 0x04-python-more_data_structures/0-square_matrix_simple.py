#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    newmatrix = [[(i * i) for i in j] for j in matrix]
    return (newmatrix)
