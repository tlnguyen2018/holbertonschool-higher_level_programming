#!/usr/bin/python3
"""
Square class with private instance attribute
"""


class Square:
    """
    Initialize the class with setter and getter for size
    """

    def __init__(self, size=0):
        """
        Initialize the class Square
        """
        self.size = size
    """
    Getter method
    """
    @property
    def size(self):
        return (self.__size)

    @size.setter
    def size(self, value):
        if type(value) != int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    """
    Area method
    """
    def area(self):
        area = self.__size * self.__size
        return (area)
