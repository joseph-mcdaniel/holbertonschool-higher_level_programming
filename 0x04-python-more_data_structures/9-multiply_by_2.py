#!/usr/bin/python3
def multiply_by_2(my_dict):
    new_dict = {}
    for value in my_dict:
        new_dict[value] = my_dict[value] * 2
    return new_dict
