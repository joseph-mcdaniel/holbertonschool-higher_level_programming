#!/usr/bin/python3
def append_write(filename="", text=""):
    with open(filename, 'a') as f:
        f.write(text)
    return len(text)
