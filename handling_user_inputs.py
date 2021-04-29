#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: ashutosh

A program to accept various inputs from user.

"""


def main():
    """
    The main function to execute upon call.

    Returns
    -------
    int
        returns integer 0 for safe executions.

    """
    # Accepting string input
    string = input("Enter any string: ")
    print("The input string:", string)

    # Accepting integer input
    integer = int(input("Enter an integer: "))
    print("The input integer:", integer)

    # Accepting floating point input
    floating = float(input("Enter a floating point number: "))
    print("The input floating point number:", floating)

    return 0


if __name__ == "__main__":
    main()
