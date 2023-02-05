#!/usr/bin/python3
"""
    Function add two integers
    Return : a + b in cast integer
"""


def add_integer(a, b=98):
    """ Function that validate th add of the twi integers """
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    return int(a + b)
