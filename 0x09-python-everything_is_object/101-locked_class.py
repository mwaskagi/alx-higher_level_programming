#!/usr/bin/python3
""" Locked Class """


class LockedClass:
    """ No Class or object attributes cant set except first name """
    def __setattr__(self, attribute, value):
        if attribute == "first_name":
            self.__dict__[attribute] = value
        else:
            raise AttributeError("'LockedClass' object has no attribute '" + attribute + "'")
