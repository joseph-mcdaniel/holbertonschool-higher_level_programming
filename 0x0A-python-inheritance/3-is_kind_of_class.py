#!/usr/bin/python3
def is_kind_of_class(obj, a_class):
    if not isinstance(obj, a_class):
        # returns false if the obj is not instance of class
        return False
    else:
        return True
