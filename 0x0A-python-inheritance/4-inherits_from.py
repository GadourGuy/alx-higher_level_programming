#!/usr/bin/python3
"""Checks if class is sub class or a class from a super class"""


def inherits_from(obj, a_class):
    """Checks for objects"""

    if isinstance(obj, a_class) and type(obj) is not a_class:
        return True
    return False
