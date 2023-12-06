#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    if not a_dictionary:
        return None
    keys = list(a_dictionary.keys())
    new = a_dictionary.copy()
    for i in keys:
        new[i] *= 2
    return new
