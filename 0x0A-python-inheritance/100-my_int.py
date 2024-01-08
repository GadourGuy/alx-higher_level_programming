#!/usr/bin/python3
"""Module for comparing"""


class MyInt(int):
    """Class MyInt that inhertied int"""

    def __eq__(self, other):
        """Equale compare"""
            return self.real != other

    def __ne__(self, other):
        """Not Equale compare"""
            return self.real == other
