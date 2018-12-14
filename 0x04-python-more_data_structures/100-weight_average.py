#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list is None:
        return (0)
    else:
        return (sum([a * b for a, b in my_list]) /
                sum([b for a, b in my_list]))
