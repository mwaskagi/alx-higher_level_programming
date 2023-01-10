#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list == []:
        return None
    tmp = my_list[0]
    for a in my_list:
        if a > tmp:
            tmp = a
    return tmp
