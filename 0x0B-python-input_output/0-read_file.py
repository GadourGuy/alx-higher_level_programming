#!/usr/bin/python3
"""Module for reading Files"""


def read_file(filename=""):
    """ reads file"""
    with open(filename, encoding="utf-8") as file:
        print(file.read(), end="")
