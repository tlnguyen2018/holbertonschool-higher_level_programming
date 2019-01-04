#!/usr/bin/python3
"""
Square class with private instance attribute
"""


class Square:
    """
    Initialize the class
    """

    def __init__(self, size=0):
        """
        if size value is not integer, raise typeerror
        """
        if type(size) != int:
            raise TypeError("size must be an integer")
            """
            If size less than 0, value error
            """
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
