#!/usr/bin/python3
"""
 Function that appends a string at the end of a file
"""


def append_write(filename="", text=""):
    """
    return file and a string append
    """

    with open(filename, 'a') as f:
        txt = f.write(text)
    f.closed
    return (txt)
