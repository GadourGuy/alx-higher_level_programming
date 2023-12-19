#!/usr/bin/python3
class Square:
    """defines a square"""

    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.__position = position

    @property
    def size(self):
        """ gets the size"""
        return self.__size

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
        return self.__position
    @position.setter
    def position(self, value):
        if not isinstance(value, tuple) | value[0] < 0 | value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """# returns square area"""
        return self.__size ** 2

    def my_print(self):
        """prints the square"""
        for i in range(0, self.size):
            k = self.position[0]
            while k != 0:
                    print(" ", end="")
                    k -= 1
            for j in range(0, self.size):
                print("#", end="\n" if j is self.size - 1 and i != j else "")
        print()
