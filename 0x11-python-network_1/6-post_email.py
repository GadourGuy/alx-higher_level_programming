#!/usr/bin/python3
"""A script that:
takes in a URL and sends a request to the URL and displays the value
- of the X-Request-Id variable"""
import sys
import requests

if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]

    payload = {'email': email}
    response = requests.post(url, data=payload)

    print(response.text)
