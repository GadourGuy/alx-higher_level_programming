#!/usr/bin/python3
"""Displays the X-Request-Id value to a fetched URL"""
import sys
import requests


if __name__ == "__main__":
    url = sys.argv[1]

    r = requests.get(url)
    print(r.headers.get("X-Request-Id"))
