#!/usr/bin/python3
def is_same_class(obj, a_class):

    if type(obj) is a_class:
        # only if obj is exactly an instance of a_class
        return True
    else:
        return False
