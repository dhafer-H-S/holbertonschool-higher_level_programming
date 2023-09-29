#!/usr/bin/python3
"""3-main.py"""


import json


def from_json_string(my_str):
    """ a function that returns the JSON representation of an object string"""
    return json.loads(my_str)
