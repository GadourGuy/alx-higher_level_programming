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
        if isinstance(attrs, list):
            for string in attrs:
                if not isinstance(string, str):
                    return self.__dict__
        return attrs.__dict__
