#!/usr/bin/python3
def write_file(filename="", text=""):
    with open(filename, 'a') as f:
        f.write(text)
    return len(text)
