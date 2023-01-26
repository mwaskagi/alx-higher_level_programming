#!/usr/bin/python3
""" Square Class."""


class Square:
    """define a Square."""

    def __str__(self):
       """print square"""
       return self.pos_print()[:-1]

    def __init__(self, size=0, position=(0, 0)):
       """ initialize the square """
       self.size = size
       self.position = position

    @property
    def size(self):
        """property of the length of a side of square """
        return self.__position

    @position.setter
    def position(self, value):
        """ set position """
        if not isinstance(value, tuple):
            raise TypeError("position must be a tuple of 2 positibe integers")
        if len(value) != 2:
            raise TypeError("position must be a tuple of 2 position integers")
        if len([i for i in value if type(i) is not int and i >= 0]) != 2:
            raise TypeError("position must be a tuple of 2 position integers")
        self.__position = value

    def area(self):
        """ area of a square """
        return self.__size ** 2

    def pos_print(self):
        """returns the printed square with position"""
        pos = ""
        if not self.size:
            return "\n"
        for w in range(self.position[1]):
            pos += "\n"
        for w in range(self.size):
            for l in range(self.position[0]):
                pos += " "
            for l in range(self.size):
                pos += "#"
            pos += "\n"
        return pos

    def my_print(self):
        """print square."""
        print(self.pos_print(), end="")
