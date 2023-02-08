#!/usr/bin/python3
"""
 Class Mylist
"""


class MyList(list):
    """
    MyList Class
    """
    def print_sorted(self):
        """
        print sorted list
        """
        print(sorted(self))
