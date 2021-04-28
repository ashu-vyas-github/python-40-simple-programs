#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: ashutosh

This is a simple program to compute factorial of a given number

"""
import numpy


def factorial(num):
  # This is a recursive function-

    if num == 1:
        return num
    else:
        return num * factorial(num - 1)


def main():

    print("Program to calculate factorial of an input positive number")

    num = numpy.uint64(input("Enter a number: "))

    if num < 0:
        print("Factorial cannot be found for negative numbers")
    elif num == 0:
        print("Factorial of 0 is 1")
    else:
        print("Factorial of", num, "is", factorial(num))

    return 0


if __name__ == "__main__":
    main()
