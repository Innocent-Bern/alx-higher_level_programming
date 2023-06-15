#!/usr/bin/python3

def search_replace(my_list, search, replace):
    rtn = []
    for i in range(len(my_list)):
        if my_list[i] == search:
            rtn.append(replace)
        else:
            rtn.append(my_list[i])
    return rtn
