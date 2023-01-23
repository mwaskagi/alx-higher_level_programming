#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    y = 0
    try:
        for a in range(0, x):
            print("{}".format(my_list[i]), end="")
            y += 1
        print("")
        return x
    except IndexError:
        print("")
        return y
