#!/usr/bin/python3
"""
Script that takes in url
Sends request
Displays body of response decoded in utf-8
"""


from sys import argv
from urllib import request, error


if __name__ == "__main__":
    try:
        with request.urlopen(argv[1]) as response:
            print(response.read().decode("utf-8"))
    except error.HTTPError as err:
        print("Error code:", err.code)
