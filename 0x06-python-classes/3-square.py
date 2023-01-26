#!/usr/bin/python3
""" Class Square that defines as square """


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

    def area(self):
        """ Cal Square Area """
        return(self.__size * self.__size)
