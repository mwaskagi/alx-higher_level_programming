#!/usr/bin/python3


def append_write(filename="", text=""):
    """
    function appends a string at end of text file
    return number of charcters
    """
    with open(filename, 'a+') as f:
        return f.write(text)
