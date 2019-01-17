#!/usr/bin/python3
"""
Previous project, plus
"""


class BaseGeometry:
    """
    Public Instance
    """
    def area(self):
        raise Exception("area() is not implemented")
    """
    Public instance method validator
    """
    def integer_validator(self, name, value):
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
