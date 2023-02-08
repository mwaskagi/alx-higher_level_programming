#!/usr/bin/python3
"""
  Define an object attribute lookup function
"""


def lookup(obj):
    """
    Return list of object attributes
    """
    return dir(obj)
