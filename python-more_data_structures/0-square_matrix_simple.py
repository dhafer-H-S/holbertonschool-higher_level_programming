#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    temp = []

    temp = [list(map(lambda x: x**2, x)) for x in matrix]
    return (temp)
