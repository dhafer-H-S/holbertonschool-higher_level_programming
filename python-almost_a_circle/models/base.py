#!/usr/bin/python3
"""module"""


class Base:
    """base class"""

    __nb_objects = 0

    def __init__(self, id=None):
        """id"""

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = self.__nb_objects
