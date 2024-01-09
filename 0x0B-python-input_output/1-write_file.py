#!/usr/bin/python3
"""module for writing in a file"""


def write_file(filename="", text=""):
    """For writing a File"""
    with open(filename, "w", encoding="utf-8") as file:
        file.write(text)
    return len(text)
