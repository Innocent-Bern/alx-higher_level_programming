#!/usr/bin/python3

def common_elements(set_1, set_2):
    rtn = []
    for i in set_1:
        if i in set_2 and i not in rtn:
            rtn.append(i)
    return rtn
