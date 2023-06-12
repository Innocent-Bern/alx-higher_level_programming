#!/usr/bin/python3

def no_c(my_string):
    rtn_str = ""
    for i in range(len(my_string)):
        if my_string[i] not in "cC":
            rtn_str += my_string[i]
    return (rtn_str)
