#!/usr/bin/python3
"""
True if objects same type with the instance or class that inherit from
False for fail
"""


def is_kind_of_class(obj, a_class):
    if isinstance(obj, a_class):
        return (True)
    else:
        return (False)
