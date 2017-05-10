#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    if my_list == []:
        return None
    if idx == 0:
        return None
    if len(my_list) < 0 or len(my_list) > 5:
        return None
    if idx > len(my_list):
        return None
    del my_list[idx]
    return my_list
