#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    for i in my_list:
        if idx >= len(my_list) or idx < 0:
            return my_list
        else:
            my_list[idx] = element
            return my_list
