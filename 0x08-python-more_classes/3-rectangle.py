#!/usr/bin/python3
""" class rectangle that defines rectangle """


class Rectangle:
    """ Rectangle class """
    def __init__(self, width=0, height=0):
        """ Construct """
        self.height = height
        self.width = width

    @property
    def width(self):
        """ Method """
        return self.__width

    @width.setter
    def width(self, value):
        """ Methode """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise TypeError("width must be >=0 ")
        self.__width = value

    @property
    def height(self):
        """ Method """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise TypeError("height must be >= 0")
    
    def area(self):
        """ Return area """
        return self.width * self.height

    def perimeter(self):
        """ Returns perimeter """
        if self.height == 0 or self.width == 0:
            return ""
        p = ""
        for i in range(sellf.height):
            for j in range(self.width):
                p += "#"
        p = p[:-1]
        return p
