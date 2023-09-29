#!/usr/bin/python3
"""
Script that takes in a url
Sends request to url
Displays the value of X-Request-Id
"""


import requests
from sys import argv

if __name__ == "__main__":
    response = requests.get(argv[1])
    print(response.headers.get("X-Request-Id"))
