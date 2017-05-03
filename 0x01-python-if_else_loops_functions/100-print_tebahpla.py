#!/usr/bin/python3
for reverse in range(122, 96, -1):
    if reverse % 2 == 0:
        print(chr(reverse), end="")
    else:
        print((chr(reverse - 32)), end="")
