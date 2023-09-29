#!/usr/bin/python3
"""
Script that takes in a letter and searches in a post request
"""


import requests
from sys import argv


if __name__ == "__main__":
    let = "" if len(argv) == 1 else argv[1]
    res = requests.post("http://0.0.0.0:5000/search_user", {"q": let})

    try:
        res = res.json()
        if res == {}:
            print("No result")
        else:
            print(f"[{res.get('id')}] {res.get('name')}")
    except ValueError:
        print("Not a valid JSON")
