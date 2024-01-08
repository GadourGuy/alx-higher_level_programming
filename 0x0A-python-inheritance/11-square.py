#!/usr/bin/python3
"""importing rectangler file"""
Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """representaion of a square object using Rectangle"""

    def __init__(self, size):
        """initiliaze a new square

        Args:
            size (int): size of a square
        """
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """"calcs area"""
        return self.__size * self.__size

    def __str__(self):
        """string representaion of a square class"""
        return "[Square] {}/{}".format(self.__size, self.__size)
