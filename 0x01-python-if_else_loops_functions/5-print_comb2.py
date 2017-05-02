#!/usr/bin/python3
for num in range(0, 100):
    if num < 10:
        print("{:02d}, ".format(num), end="")
    elif num < 99:
        print("{:d}, ".format(num), end="")
    else:
        print("{:d}".format(num))
