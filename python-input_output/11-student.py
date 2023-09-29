#!/usr/bin/python3
"""student module"""


class Student:
    """student class """

    def __init__(self, first_name, last_name, age):

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """a dictionary for student data"""
        if attrs is None:
            return self.__dict__
        newdict = {}
        for i in attrs:
            try:
                newdict[i] = self.__dict__[i]
            except BaseException:
                pass

        return newdict

    def reload_from_json(self, json):
        """update from old database"""

        for y in json:
            self.__dict__.update({y: json[y]})
