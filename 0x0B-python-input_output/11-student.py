#!/usr/bin/python3
"""
Student class
"""


class Student:
    """
    Student class
    """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        return student dictionary
        """
        tmp = {}
        if attrs is None:
            return self.__dict__
        tmp = dict()
        """
        retrieve names from list
        """
        for key in attrs:
            if key in self.__dict__.keys():
                tmp[key] = self.__dict__[key]
        return tmp

    def reload_from_json(self, json):
        """
        replace all attributes of student instance
        """
        return self.__dict__.update(json)
