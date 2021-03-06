#!/usr/bin/python3
"""
Write a class Rectangle that defines a rectangle:
Private instance attribute: width:
property def width(self): to retrieve it
property setter def width(self, value): to set it:
width must be an integer, otherwise TypeError message width must be an integer
if width is less than 0, raise ValueError message width must be >= 0
Private instance attribute: height:
property def height(self): to retrieve it
property setter def height(self, value): to set it:
height must be an integer, otherwise TypeError
message height must be an integer
if height is less than 0, raise ValueError message height must be >= 0
"""


class Rectangle:
    """
    define class Rectangle
    """
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    """
    setter -getter for private instance width
    """
    @property
    def width(self):
        return (self.__width)

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    """
    setter - getter for private instance height
    """
    @property
    def height(self):
        return (self.__height)

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >=0")
        self.__height = value
