#!/usr/bin/python3
"""
Square class with private instance attribute
"""


class Square:
    """
    Initialize the class with setter and getter for size
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Initialize the class Square
        """
        self.size = size
        self.position = position
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
    Getter method position
    """
    def position(self):
        return (self.__position)

    """
    Position method setter
    """
    def position(self, value):
        if type(value) != tuple:
            raise TypeError('position must be a tuple of 2 positive integers')
        elif len(value) != 2:
            raise TypeError('position must be a tuple of 2 positive integers')
        elif type(value[0]) != int or type(value[1]) != int:
            raise TypeError('position must be a tuple of 2 positive integers')
        elif value[0] < 0 or value[1] < 0:
            raise TypeError('position must be a tuple of 2 positive integers')
        else:
            self.__position = value

    """
    Area method
    """
    def area(self):
        area = self.__size * self.__size
        return (area)
    """
    Public instance method prints in stdout the square with the character #
    """
    def my_print(self):
        if self.__size is 0:
            print()
        else:
            x, y = self.position
            for i in range(y):
                print()
            for i in range(self.size):
                print('_' * x, end='')
                print('#' * self.size)
