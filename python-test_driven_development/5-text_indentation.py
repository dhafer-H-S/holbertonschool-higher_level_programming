#!/usr/bin/python3

"""
a function that prints 2 new lines after thi characters".?:"
"""


def text_indentation(text):
    """ a function that prints 2 new lines after thi characters
    Args:
        text: string
    Returns:
        0
    Raise:
        TypeError: If text is not a string
    """

    if type(text) is not str:
        raise TypeError("text must be a string")

    s = text[:]

    for char in ".?:":
        list_text = s.split(char)
        s = ""
        for i in list_text:
            i = i.strip(" ")
            s = i + char if s == "" else s + "\n\n" + i + char

    print(s[:-3], end="")
