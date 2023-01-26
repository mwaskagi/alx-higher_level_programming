#!/usr/bin/python3
""" Class square that defines a square """


class Square:
    """ Square Class """
    def __init__(self, size=0):
        """ Constructor """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
