#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    rtn = {}
    for i in a_dictionary:
        rtn.update({i: a_dictionary[i] * 2})
    return rtn
