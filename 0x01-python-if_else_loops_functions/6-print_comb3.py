#!/usr/bin/python3
for i in range(100):
    if ((i % 10) * 10) + (i // 10) > i:
        if i + 1 == 90:
            print(89)
        else:
            print("{:02d}".format(i), end=", ")
