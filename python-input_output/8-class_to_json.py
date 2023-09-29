#!/usr/bin/python3
"""return dictionary"""


def class_to_json(obj):
    """a function that returns the dictionary with data JSON serialization"""
    return obj.__dict__
