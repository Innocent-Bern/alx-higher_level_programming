#!/usr/bin/python3
"""
Script that takes in a url and email
Sends Post req to url with email as a parameter
displays body of response decoded in uft-8
"""


import requests
from sys import argv


if __name__ == "__main__":
    response = requests.post(argv[1], argv[2])
    print(response.text)
