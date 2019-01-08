#!/usr/bin/python3


"""
Addition python program for a and b
Using doctest
"""


def add_integer(a, b=98):
    """
    Condition: a and b must be integers or floats,
    otherwise raise a TypeError exception with the message
    a must be an integer or b must be an integer
    a and b must be first casted to integers if they are float
    Returns an integer: the addition of a and b
    """
    if not (isinstance(a, float) or isinstance(a, int)):
        raise TypeError("a must be an integer")
    if not (isinstance(b, float) or isinstance(b, int)):
        raise TypeError("b must be an integer")
    return int(a + b)
