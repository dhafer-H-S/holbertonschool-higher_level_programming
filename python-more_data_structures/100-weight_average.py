#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list and len(my_list):
        sum = 0
        val = 0
        for sub in my_list:
            sum = sum + (sub[0] * sub[1])
            val = sub[1] + val
        return (sum / val)
    return (0)
