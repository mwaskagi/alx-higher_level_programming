#!/usr/bin/python3
""" Class Square that defines a square """


class Square:
    """ Class Square """
    def __init___(self, size=0):
        """ Module validation """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """ Method return areas """
        return(self.__size ** 2)

    @property
    def size(self):
        """ Method property of size, return size """
        return self.__size

    @size_setter
    def size(self, value):
        """ Method size_setter attribute evlauate the value """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value
