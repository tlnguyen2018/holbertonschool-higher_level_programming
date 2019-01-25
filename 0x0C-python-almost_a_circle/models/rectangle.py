#!/usr/bin/python3
"""
Rectangle inherit from Base
"""
from models.base import Base


class Rectangle(Base):
    """
    class Rectangle inherit from Base class
    initiate class constructor
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        super class id
        """
        super().__init__(id)
        """
        argument list
        """
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        return (self.__width)

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        else:
            if (value > 0):
                self.__width = value
            else:
                raise ValueError("width must be > 0")

    @property
    def height(self):
        return (self.__height)

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        else:
            if (value > 0):
                self.__height = value
            else:
                raise ValueError("height must be > 0")
    """
    setter getter of x , y
    """
    @property
    def x(self):
        return (self.__x)

    @x.setter
    def x(self, value):
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        else:
            if (value >= 0):
                self.__x = value
            else:
                raise ValueError("x must be >= 0")

    @property
    def y(self):
        return (self.__y)

    @y.setter
    def y(self, value):
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        else:
            if (value >= 0):
                self.__y = value
            else:
                raise ValueError("y must be >= 0")
