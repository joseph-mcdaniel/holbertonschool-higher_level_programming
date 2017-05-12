#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    newmatrix = [
        [element**2 for element in row]
        for row in matrix
    ]
    return newmatrix
