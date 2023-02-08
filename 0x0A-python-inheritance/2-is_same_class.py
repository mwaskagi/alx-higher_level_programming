#!/usr/bin/python3
"""
Class is_same_clas funtion 
"""

def is_same_class(obj, a_class):
    """
    checks if object is similar as instance of a given class
    Return true if same else false
    """
    if type(obj) == a_class:
        return True
    return False
