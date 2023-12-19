#!/usr/bin/python3
"""Square class that has size"""


class Square:
    """defines a square"""

    def __init__(self, size=0):
        self.__size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if isinstance(value, int) and value >= 0:
            self.__size = value
        else:
            raise TypeError("size must be an integer")
        if int(value) < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """# returns square area"""
        return self.__size ** 2

    def my_print(self):
        """prints the square"""

        if self.__size == 0:
            print()
        else:
            for i in range(0, self.__size):
                for j in range(0, self.__size):
                    print("#", end="")
        print()
