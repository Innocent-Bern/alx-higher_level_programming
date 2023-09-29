#!/usr/bin/python3
"""
Script that takes in url
Sends request
Displays body of response decoded in utf-8
"""


from sys import argv
import requests


if __name__ == "__main__":
    response = requests.get(argv[1])

    if response.status_code >= 400:
        print(f"Error code: {response.status_code}")
    else:
        print(response.text)
