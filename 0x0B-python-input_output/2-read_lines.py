#!/usr/bin/python3
def read_lines(filename="", nb_lines=0):
    with open("my_file_0.txt", "r") as f:
        if nb_lines <= 0 or nb_lines >= len(f.readlines()):
            x =  f.read()
            print(x)
        else:
            print(f.readline())
