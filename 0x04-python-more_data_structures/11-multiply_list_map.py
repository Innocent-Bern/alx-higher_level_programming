#!/usr/bin/python3

def multiply_list_map(my_list=[], number=0):
    def mul(el):
        return el * number
    return list(map(mul, my_list))
