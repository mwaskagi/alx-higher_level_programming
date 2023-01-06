#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    x = 1
    num = 0
    while x != len(argv):
        a = argv[x]
        num += int(a)
        x += 1
    print("{:d}".format(num))
