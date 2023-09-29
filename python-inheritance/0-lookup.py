#!/usr/bin/python3
""" module for lookup"""


def lookup(obj):
    '''Lookup object attributes and methods.
    Args:
        obj to list.
    Return:
        list of attributes.
    '''
    return dir(obj)
