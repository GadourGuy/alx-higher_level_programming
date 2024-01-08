#!/usr/bin/python3
"""Module for basic geometry"""


class BaseGeometry:
    """calculates basic geometry"""

    def area(self):
        """raises an error"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """raises errors for values"""

        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
