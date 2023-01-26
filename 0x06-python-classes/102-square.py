#!/usr/bin/python3
""" Class defines a square """


class Square:
    """Class Square """

    def __init__(self, size=0):
        """ initialize attribute size """
        self.size = size

    def area(self):
        """ Cal area """
        return self.__size ** 2

    @property
    def size(self):
        """ Get size """
        return self.__size

    @size.setter
    def size(self. value):
        """ set size """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def __eq__(self, other):
        """Compare """
        return self.size == other.size
    
    def __ne__(self, other):
        """ Not Equal """
        return self.size != other.size

    def __lt__(self, other):
        """ Less Than """
        return self.size < other.size

    def __le__(self, other):
        """ less than or equal to """
        return self.size <= other.size

    def  __gt__(self, other):
        """ Greater Than """
        return self.size > other.size

    def __ge__(self, other):
        """ Greater than or equal """
        return self.size >= other.size
