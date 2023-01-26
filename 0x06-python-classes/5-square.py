#!/usr/bin/python3
""" Class Square define square """


class Square:
    """ Square class """
    def __init__(self, size=0):
        """ Method """
        self.__size = size

    def area(self):
        """ Area Method """
        return(self.__size ** 2)

    @property
    def size(self):
        """ Property of size """
        return self.__size

    @size.setter
    def size(self, value):
        """ setter """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def my_print(self):
        """ Method my_print to print squeare """
        if self.__size == 0:
            print("")
            return
        for i in range(0, self.__size):
            for j in range(0, self.__size):
                print("#", end="")
            print("")
