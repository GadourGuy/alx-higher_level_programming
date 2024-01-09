#!/usr/bin/python3
"""Module for creating student class”"""


class Student:
    """Student class with first and last names"""

    def __init__(self, first_name, last_name, age):
        """ATrributes: firstname, lastname, age"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """dictionary represtaion of a class"""
        if type(attrs) == list:
            for string in attrs:
                if type(string) != str:
                    return self.__dict__
        return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
