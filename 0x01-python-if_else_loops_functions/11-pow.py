#!/usr/bin/python3
def pow(a, b):
    if b == 0:
        return 1
    elif b > 0:
        for i in range(b - 1):
            a *= a
    elif b < 0:
        for i in range(b * -1 - 1):
            a = a * a
        a = 1 / a
    return a
