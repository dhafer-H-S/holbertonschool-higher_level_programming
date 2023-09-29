#!/usr/bin/python3
"""write an object"""


import json


def save_to_json_file(my_obj, filename):
    """a function that writes an Object to a text file using a JSON"""
    with open(filename, "w", encoding="utf-8") as filename:
        filename.write(json.dumps(my_obj))
