#!/usr/bin/python3
""" Define Class Square """


class Square:
    """ Define class square """
    def __init__(self, size=0, position=(0, 0)):
        """ initialize square """
        self.__size = size
        self.__position = position

    @property
    def size(self):
        """ set current size of square """
        return self.__size

    @size.setter
    def size(self, value):
        """ Sice setter """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        """ setcurrent positon """
        return self.__position

    @position.setter
    def position(self, value):
        """ Setter position """
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif type(value[0]) is not int or type(value[1]) is not int:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """ Cal Area """
        return(self.__size ** 2)

    def my_print(self):
        """ print square """
        if self.size != 0:
            for p in range(0, self.__position[1]):
                print("")
            for s in range(0, self.__size):
                [print(" ", end="") for t in range(0, self.__position[0])]
                [print("#", end="") for u in range(0, self.__size)]
                print("")
        else:
            print("")
