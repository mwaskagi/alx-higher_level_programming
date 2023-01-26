#!/usr/bin/python3
""" Class Square that defines a square """


class Square:
    """ Class Square """
    def __init___(self, size=0):
        """ Constructor """
        self.__size = size

    @property
    def size(self):
        """ Method property of size, return size """
        return self.__size

    @size_setter
    def size(self, value):
        """ Method size_setter attribute evlauate the value """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """ Cal Area """
        return(self.__size * self.__size)
