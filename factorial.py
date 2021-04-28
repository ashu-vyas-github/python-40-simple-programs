#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: ashutosh

This is a simple program to compute factorial of a given number

"""
import numpy

# This is a recursive function


def factorial(num):
    """
    This function calculates factorial of a number recursively.

    n! = n*(n-1)*(n-2)*...*2*1

    Parameters
    ----------
    num : uint64
        Input positive integer to calcuate factorial.

    Returns
    -------
    uint64
        Factorial of input positive integer.

    """

    if num == 1:
        return num
    else:
        return num * factorial(num - 1)


def main():
    """
    The main function to execute upon call.

    Returns
    -------
    int
        returns integer 0 for safe executions.

    """

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
