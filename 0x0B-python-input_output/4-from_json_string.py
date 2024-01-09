#!/usr/bin/python3
"""module for the JSON representation of an object """
import json


def from_json_string(my_str):
    """returns the JSON representation of an object"""
    return json.loads(my_str)
