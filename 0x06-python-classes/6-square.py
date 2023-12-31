#!/usr/bin/python3
"""define a square class"""


class Square:
    """defines a square"""

    def __init__(self, size=0, position=(0, 0)):
        """initialize a new square.
        Args:
            size (int): size of sqare.
            position (int, int): position of square.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """ gets the size"""
        return (self.__size)

    @size.setter
    def size(self, value):
        if isinstance(value, int) and value >= 0:
            self.__size = value
        else:
            raise TypeError("size must be an integer")
        if int(value) < 0:
            raise ValueError("size must be >= 0")

    @property
    def position(self):
        """gets the position"""
        return (self.__position)

    @position.setter
    def position(self, value):
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """# returns square area"""
        return (self.__size * self.__size)

    def my_print(self):
        """prints the square"""
        if self.__size == 0:
            print("")
            return
        [print("") for i in range(0, self.__position[1])]
        for i in range(0, self.__size):
            [print(" ", end="") for j in range(0, self.__position[0])]
            [print("#", end="") for k in range(0, self.__size)]
            print("")
