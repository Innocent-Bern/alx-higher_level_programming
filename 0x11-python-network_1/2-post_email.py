#!/usr/bin/python3
"""
Script that takes in a url and email
Sends Post req to url with email as a parameter
displays body of response decoded in uft-8
"""


from urllib import request, parse
from sys import argv


if __name__ == "__main__":
    data = parse.urlencode({"email": argv[2]}).encode()
    req = request.Request(argv[1], data=data)

    with request.urlopen(req) as response:
        print(response.read().decode("utf-8"))
