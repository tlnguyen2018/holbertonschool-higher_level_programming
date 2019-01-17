#!/usr/bin/python3
"""
Previous project, plus
class Rectangle inherit from BaseGeometry
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


class Rectangle(BaseGeometry):
    """
    Rectangle is subclass
    Instantiation with width and height, private
    """
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
