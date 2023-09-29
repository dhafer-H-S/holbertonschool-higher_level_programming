#!/usr/bin/python3
def uniq_add(my_list=[]):
    list_n = set(my_list)
    res = 0
    for x in list_n:
        res = res + x
    return (res)
