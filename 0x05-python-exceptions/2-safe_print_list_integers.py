#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    count = 0
    try:
        for i in my_list:
            if int(i):
                print("{:d}".format(i), end="")
            elif i[0] in ["+", "-"]:
                if any(char is not char.isdigit() for char in i[1:]):
                    count += 1
                    continue
                else:
                    print("{}{:d}".format(i[0], i[1:]), end="")
            else:
                if any(char is not char.isdigit() for char in i):
                    count += 1
                    continue
                else:
                    print("{:d}".format(i), end="")
            count += 1
    except IndexError:
        print("IndexError: list index out of range")
    finally:
        print()
        return count
