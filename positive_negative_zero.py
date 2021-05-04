# -*- coding: utf-8 -*-
"""
@author: ashutosh

Program to check positive, negative, or zero input.

"""


def check_number_sign():
    """
    Checks the sign of the input number.

    Returns
    -------
    None.
        Sign check result.

    """

    number = float(input("Enter number: "))  # accept input from user

    # checking the number
    if number < 0:
        print("{n1} is negative.".format(n1=number))
    elif number > 0:
        print("{n1} is positive.".format(n1=number))
    elif number == 0:
        print("{n1} is zero.".format(n1=number))
    else:
        print("{n1} is not a number".format(n1=number))

    return 0


def main():
    """
    The main function to execute upon call.

    Returns
    -------
    int
        returns integer 0 for safe executions.

    """

    print("Program to check positive, negative, or zero input.")

    temp = check_number_sign()

    return 0


if __name__ == "__main__":
    main()
