#!/usr/bin/python3
"""Module for creating an Object from a “JSON file”"""
import json


def load_from_json_file(filename):
    """creates an object from a jason file"""
    with open(filename, encoding="uft-8") as file:
        json.loads(file.read())
