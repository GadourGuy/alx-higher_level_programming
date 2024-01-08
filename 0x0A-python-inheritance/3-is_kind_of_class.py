#!/usr/bin/python3
"""Checks if class is sub class or a class from a super class"""


def is_kind_of_class(obj, a_class):
    """Checks for objects"""

    if isinstance(obj, a_class):
        return True
    return False
