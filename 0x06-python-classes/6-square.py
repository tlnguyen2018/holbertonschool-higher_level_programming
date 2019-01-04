#!/usr/bin/python3
class Square:
    """
    Create class Square
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        initialization method size and position
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """
        getter size
        """
        return (self.__size)

    @size.setter
    def size(self, value):
        """
        setter size
        """
        if type(value) != int:
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = value

    @property
    def position(self):
        """
        getter position
        """
        return (self.__position)

    @position.setter
    def position(self, value):
        """
        position setter
        """
        if (type(value) != tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif (len(value) != 2):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif (type(value[0]) != int or type(value[1]) != int):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif (value[0] < 0 or value[1] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """
        Square area
        """
        return (self.__size * self._size)

    def my_print(self):
        """
        prints to stdout square with the char #
        """
        if self.size == 0:
            print()
        else:
            """
            a, b = self.position
            for line in range(b):
                print()
            for line in range(self.size):
                print(' ' * a, end='')
                print('#' * self.size)
            """
            for p in range(0, self.__position[1]):
                print("")
            for i in range(0, self.__size):
                for p in range(0, self.__position[0]):
                    print(" ", end="")
                for i in range(0, self.__size):
                    print("#", end="")
            print("")
