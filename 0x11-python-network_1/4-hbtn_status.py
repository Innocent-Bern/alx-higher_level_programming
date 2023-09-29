#!/usr/bin/python3
"""
script that fetches https://alx-intranet.hbtn.io/status
"""


import requests


if __name__ == "__main__":
    res = requests.get("https://alx-intranet.hbtn.io/status")
    print(f"""Body response:
    \t- type: {type(res.text)}
    \t- content: {res.text}""")
