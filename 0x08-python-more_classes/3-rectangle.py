#!/usr/bin/python3
"""
Same as the previous task
ADDING:
Public instance method: def perimeter(self): returns the rectangle perimeter:
if width or height is equal to 0, perimeter has to be equal to 0
print() and str() should print the rectangle with the character #:
if width or height is equal to 0, return an empty string
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

    """
    use str
    """
    def __str__(self):
        if self.__width is 0 or self.__height is 0:
            return ""
        for row in range(self.__height -1):
            print("#" * self.__width)
        return ("#" * self.__width)
