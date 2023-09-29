#!/usr/bin/python3
"""
Script that takes in a url and email
Sends Post req to url with email as a parameter
displays body of response decoded in uft-8
"""


import urllib.request
import urllib.parse
from sys import argv


if __name__ == "__main__":
    data = urllib.parse.urlencode({"email": argv[2]}).encode("ascii")
    req = urllib.request.Request(argv[1], data)

    with urllib.request.urlopen(req) as response:
        print(response.read().decode("utf-8"))
