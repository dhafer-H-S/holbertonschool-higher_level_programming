#!/usr/bin/python3
"""Funtion adds 2 integers"""


def add_integer(a, b=98):
    """ Function that adds two strings.
    Args: a (int) and  b (int)
    Returns: The sum
    """
    if (not isinstance(a, int) and not isinstance(a, float)) or a != a:
        raise TypeError("a must be an integer")
    if not isinstance(b, int) and not isinstance(b, float) or b != b:
        raise TypeError("b must be an integer")
    return int(a) + int(b)
