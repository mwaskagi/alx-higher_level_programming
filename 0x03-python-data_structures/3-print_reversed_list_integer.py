#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if my_list:
        i = 0
        my_list.reverse()
        while i < len(my_lsit):
            print("{:d}".format(my_list[i]))
            i += 1
