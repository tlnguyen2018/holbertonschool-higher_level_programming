#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):

    if (my_list is not None and len(my_list) > 0):
        a = len(my_list) - 1
        for integer in my_list:
            print("{:d}".format(my_list[a]))
            a -= 1
