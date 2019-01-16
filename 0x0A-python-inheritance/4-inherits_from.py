#!/usr/bin/python3
"""
Check if the object is an instance of a class that inherited from
specific class
"""


def inherits_from(obj, a_class):
    if type(obj) is a_class:
        return (False)
    if isinstance(obj, a_class):
        return (True)
