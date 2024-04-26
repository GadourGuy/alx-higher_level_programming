#!/usr/bin/python3
"""A script that:
- takes in a letter and sends POST request
"""
import sys
import requests


if __name__ == "__main__":
    letter = "" if len(sys.argv) == 1 else sys.argv[1]
    payload = {"q": letter}

    result = requests.post("http://0.0.0.0:5000/search_user", data=payload)
    try:
        response = result.json()
        if response == {}:
            print("No result")
        else:
            print("[{}] {}".format(response.get("id"), response.get("name")))
    except ValueError:
        print("Not a valid JSON")
