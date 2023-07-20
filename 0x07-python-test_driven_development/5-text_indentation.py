#!/usr/bin/python3
"""function module"""


def text_indentation(text):
    """prints text with 2 newline after ? or :"""

    if type(text) is not str:
        raise TypeError("text must be a string")
    count = 0
    for x in text:
        if x in "?:.":
            print(f"{x}\n", sep="")
        else:
            if x == " " and text[count - 1] in "?:.":
                pass
            else:
                print(x, end="")
        count += 1
