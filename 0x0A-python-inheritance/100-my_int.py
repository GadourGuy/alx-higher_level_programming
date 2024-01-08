#!/usr/bin/python3
"""Module for comparing"""


class MyInt(int):
    """Class MyInt that inhertied int"""

    def __eq__(self, value):
        """Equale compare"""
            return self.real != value

    def __ne__(self, value):
        """Not Equale compare"""
            return self.real == value
