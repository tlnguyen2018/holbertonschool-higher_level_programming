#!/usr/bin/python3
"""
Private instance attribute: width:
private def width(self)
setter def width(self, value)
width must be an integer, TypeError "width must be an integer"
width is less than 0, ValueError "width must be >= 0"
Private instance attribute: height:
def height(self): to retrieve it
setter def height(self, value): to set it:
height must be an integer, TypeError"height must be an integer"
if height is less than 0,ValueError"height must be >= 0"
def __init__(self, width=0, height=0):
Public instance method: def area(self): that returns the rectangle area
Public instance method: def perimeter(self): returns the rectangle perimeter:
if width or height is equal to 0, perimeter is equal to 0
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

    """
    Public instance Area
    """
    def area(self):
        return (self.__width * self.__height)

    """
    Public instance Perimeter
    """
    def perimeter(self):
        perimeter = (self.__width + self.__height) * 2
        if self.__width is 0 or self.__height is 0:
            return 0
        return (perimeter)
