#!/usr/bin/python3
for reverse in range(122, 96, -1):
    if reverse % 2 != 0:
        reverse -= 32
    print("{}".format(chr(reverse)), end="")
