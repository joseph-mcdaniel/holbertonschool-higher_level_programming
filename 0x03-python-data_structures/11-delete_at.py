#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    if my_list == []:
        return None
    if idx == 0:
        return None
    del my_list[idx]
    return my_list
