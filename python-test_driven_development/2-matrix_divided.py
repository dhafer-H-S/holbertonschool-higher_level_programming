#!/usr/bin/python3


"""
This is a function that divides all elements of a matrix
"""


def matrix_divided(matrix, div):
    """ a function that divides all elements of a matrix
    Args:
        matrix :  lists of integers or floats
        div: number which divides the matrix
    Returns:
        new matrix
    Raises:
        TypeError: If the elements of the matrix are not a  list
                   If the elemetns of the lists are not  integers or floats
                   If div is not an integer or float number
                   If the lists of the matrix dosen't have the same size
        ZeroDivisionError: If div is 0
    """

    matrix_msg = "matrix must be a matrix (list of lists) of integers/floats"

    if not matrix or not isinstance(matrix, list):
        raise TypeError(matrix_msg)

    rowsize = 0
    rowmsg = "Each row of the matrix must have the same size"

    for elems in matrix:
        if not elems or not isinstance(elems, list):
            raise TypeError(matrix_msg)

        if rowsize != 0 and len(elems) != rowsize:
            raise TypeError(rowmsg)

        for num in elems:
            if not type(num) in (int, float):
                raise TypeError(matrix_msg)

        rowsize = len(elems)

    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    re = list(map(lambda x: list(map(lambda y: round(y / div, 2), x)), matrix))
    return (re)
