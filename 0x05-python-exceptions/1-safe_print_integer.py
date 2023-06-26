#!/usr/bin/python3

def safe_print_integer(value):
    try:
        if int(value):
            print("{:d}".format(value))
            return True
        elif value[0] in ["+", "-"]:
            if any(char is not char.isdigit() for char in value[1:]):
                raise ValueError
            else:
                print("-{:d}".format(value[1:]))
        else:
            if any(char is not char.isdigit() for char in value):
                raise ValueError
            else:
                print("{:d}".format(value))
    except ValueError:
        return False
