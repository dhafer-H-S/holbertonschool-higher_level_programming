#!/usr/bin/python3
"""write srting"""


def write_file(filename="", text=""):
    """ a function that writes a string to a text file (UTF8)"""
    with open(filename, "w", encoding="utf-8") as filename:
        return filename.write(text)
