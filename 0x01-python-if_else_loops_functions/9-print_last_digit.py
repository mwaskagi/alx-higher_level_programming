#!/usr/bin/python3
def print_last_digit(number):
    if number < 0:
        y = number * -1
        y = y % 10
    else:
        y = number % 10
    print('{:d}'.format(y), end="")
    return y
