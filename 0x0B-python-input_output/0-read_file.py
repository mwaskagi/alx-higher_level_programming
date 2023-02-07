#!/usr/bin/python3
"""
function that reads a text file and prints it
"""


def read_file(filename=""):
    """
    readfile: read a file using with
    Args:
        filename(str): filename
    """
    with open(filename, 'r') as f:
        print(f.read(), end="")
