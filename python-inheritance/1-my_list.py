#!/usr/bin/python3
""" module for Mylist class"""


class MyList(list):
    """ class of  list """

    def print_sorted(self):
        """ print the list but sorted"""
        print(sorted(self))
