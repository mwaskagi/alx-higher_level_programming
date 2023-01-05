#!/usr/bin/python3
def fizzbuzz():
    x = "Fizz"
    y = "Buzz"
    z = "FizzBuzz"
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print("{:s}".format(z), end=" ")
            continue
        if i % 3 == 0:
            print("{:s}",format(x), end=" ")
            continue
        if i % 5 == 0:
            print("{:s}",format(y), end=" ")
            continue
        print("{:d}".format(i), end=" ")
