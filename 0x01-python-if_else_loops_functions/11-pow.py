#!/usr/bin/python3
def pow(a, b):
    c = 1
    for i in range(b):
        c *= a
    if b < 0:
        return 1 / c
    return c
