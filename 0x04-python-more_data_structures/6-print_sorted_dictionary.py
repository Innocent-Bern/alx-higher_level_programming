#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    ky_list = list(a_dictionary.keys())
    ky_list.sort()
    for i in ky_list:
        print(f"{i}: {a_dictionary[i]}")
