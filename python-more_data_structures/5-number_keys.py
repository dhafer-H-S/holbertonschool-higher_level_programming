#!/usr/bin/python3
def number_keys(a_dictionary):
    res = 0
    for key in a_dictionary:
        if a_dictionary[key] != 0:
            res = res + 1
    return(res)
