#!/usr/bin/python3
def number_of_lines(filename=""):
    with open(filename, "r", encoding="utf-8") as f:
        lines = len(f.readlines())
    return lines
