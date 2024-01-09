#!/usr/bin/python3
"""Module for creating an Object from a “JSON file”"""
import json
import sys


save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
json_list = sys.argv[1:]
try:
    old = load_from_json_file("add_item.json")
    save_to_json_file(old + json_list, "add_item.json")
except FileNotFoundError:
    save_to_json_file(json_list, "add_item.json")
