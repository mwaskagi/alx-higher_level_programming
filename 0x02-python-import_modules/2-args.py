#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    x = 1
    if len(argv) == 1:
        print("{:d} arguments.".format(len(argv) - 1))
    elif len(argv) == 2:
        print("{:d} argument:".format(len(argv) - 1))
    else:
        print("{:d} arguments:".format(len(argv) - 1))
    while x != len(argv):
        a = argv[x]
        print("{:d}: {:s}".format(x, str(a)))
        x += 1
