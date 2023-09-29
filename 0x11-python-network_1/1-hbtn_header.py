#!/usr/bin/python3
"""
Script that takes in a url
Sends request to url
Displays the value of X-Request-Id
"""


import urllib.request
import sys


with urllib.request.urlopen(sys.argv[1]) as response:
    print(dict(response.headers).get("X-Request-Id"))
