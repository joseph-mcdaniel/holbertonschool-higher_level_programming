#!/usr/bin/python3
def print_square(size):
    # check if size is int
    if not isinstance(size, int):
        raise TypeError("size must be integer")
    # check if size is < 0
    if size < 0:
        raise ValueError("size must be >= 0")
    # print square
    for i in range(size):
        print("{:s}".format("#" * size))
