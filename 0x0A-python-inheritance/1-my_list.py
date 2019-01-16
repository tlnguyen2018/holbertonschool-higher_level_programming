#!/usr/bin/python3
"""
Write class MyList that inherits from list
Public instance method print_sorted(self) that sorted print out
"""


class MyList(list):
    """
    subclass MyList, super class list
    """
    def print_sorted(self):
        print(sorted(self))
