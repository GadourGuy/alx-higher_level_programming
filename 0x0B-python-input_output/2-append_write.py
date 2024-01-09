#!/usr/bin/python3
"""module for writing in a file"""


def append_write(filename="", text=""):
    """For writing a File"""
    count = 0
    with open(filename, "a", encoding="utf-8") as file:
        return file.write(text)
