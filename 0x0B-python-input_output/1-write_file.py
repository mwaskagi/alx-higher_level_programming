#!/usr/bin/python3
"""
function that writes a string to a text file
"""


def write_file(filename="", text=""):
    """
    Return the number of charcters written
    """
    with open(filename, 'w') as f:
        return f.write(text)
