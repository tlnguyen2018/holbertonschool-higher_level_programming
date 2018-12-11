#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
   if (my_list is not None and len(my_list) > 0):
       i = (len(my_list) - 1)
       for integer in my_list:
           print("{:d}".format(my_list[i]))
           i = i - 1
