# -*- coding: utf-8 -*-
"""
@author: ashutosh

A simple program to add two numbers.

"""


def main():
    """
    The main function to execute upon call.

    Returns
    -------
    int
        returns integer 0 for safe executions.

    """

    print("Program to add two numbers.\n")

    # two float values
    num1 = 1.5
    num2 = 4.5

    # Adding the two given numbers
    sum_val = float(num1) + float(num2)

    # Displaying the result
    print("The sum of given numbers is,")
    print("{n1} + {n2} = {sm}".format(n1=num1, n2=num2, sm=sum_val))

    return 0


if __name__ == "__main__":
    main()
