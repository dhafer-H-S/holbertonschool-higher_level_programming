#!/usr/bin/python3
""" module for inherits """


def inherits_from(obj, a_class):
    """return if the object in one of class that s inherted"""
    return isinstance(obj, a_class) and type(obj) != a_class
