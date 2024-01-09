#!/usr/bin/python3
"""Module for writing an Object to a text file, using a JSON"""
import json


def save_to_json_file(my_obj, filename):
    """Saves a file and writes a JSON represtaion for it"""
    with open(filename, "w", encoding="utf-8") as file:
        file.write(json.dumps(my_obj))
