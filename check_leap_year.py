# -*- coding: utf-8 -*-
"""
@author: ashutosh

Python program to check if year is a leap year or not

"""


def main():
    """
    The main function to execute upon call.

    Returns
    -------
    int
        returns integer 0 for safe executions.

    """

    print("Program to check for leap year.")

    year = int(input("Enter a year: "))

    if (year % 4) == 0:
        if (year % 100) == 0:
            if (year % 400) == 0:
                print("{yr} is a leap year".format(yr=year))
            else:
                print("{yr} is not a leap year".format(yr=year))
        else:
            print("{yr} is a leap year".format(yr=year))
    else:
        print("{yr} is not a leap year".format(yr=year))

    return 0


if __name__ == "__main__":
    main()
