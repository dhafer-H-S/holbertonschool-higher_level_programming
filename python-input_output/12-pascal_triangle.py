#!/usr/bin/python3
""" pascal triangle"""


def pascal_triangle(n):
    """ Pascal’s triangle of n"""
    if n <= 0:
        return []

    triangle = [[1]]
    while len(triangle) != n:
        ntri = triangle[-1]
        tmp = [1]
        for i in range(len(ntri) - 1):
            tmp.append(ntri[i] + ntri[i + 1])
        tmp.append(1)
        triangle.append(tmp)
    return triangle
