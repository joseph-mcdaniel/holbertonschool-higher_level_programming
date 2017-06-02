#!/usr/bin/python3
def number_of_lines(filename=""):
    with open("my_file_0.txt", "r") as f:
        lines = len(f.readlines())
    return lines
