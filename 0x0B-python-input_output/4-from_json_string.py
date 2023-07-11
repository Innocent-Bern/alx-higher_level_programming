#!/usr/bin/python3
"""function module"""


import json


def from_json_string(my_str):
    """convert string to json object"""

    return json.loads(my_str)
