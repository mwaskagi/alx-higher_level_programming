#!/usr/bin/python3
def read_file(filename=""):
    """
    Readfile content
    Args:
        filename(str): filename
    """
    with open(filename, 'r', encoding="utf-8") as a_file:
        print"{}".format(a_file.read()), end="")
