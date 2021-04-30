# -*- coding: utf-8 -*-
"""
@author: ashutosh

A simple program to check even or odd number.

"""


def main():
    """
    The main function to execute upon call.

    Returns
    -------
    int
        returns integer 0 for safe executions.

    """

    print("Program to check even or odd number.")

    num = int(input("Enter any integer number: "))
    flag_even_odd = num % 2

    if flag_even_odd == 0:
        print("{nm} is even number.".format(nm=num))
    elif flag_even_odd == 1:
        print("{nm} is odd number.".format(nm=num))
    else:
        print("Enter only integers.")

    return 0


if __name__ == "__main__":
    main()
