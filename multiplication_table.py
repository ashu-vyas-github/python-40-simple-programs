# -*- coding: utf-8 -*-
"""
@author: ashutosh

Program to print multiplication table of a number.

"""


def main():
    """
    The main function to execute upon call.

    Returns
    -------
    int
        returns integer 0 for safe executions.

    """

    print("Program to print multiplication table of a number.")

    number = float(input("Enter the number: "))
    num_elements = int(input("Number of elements: "))

    print("Multiplication table of", number)
    for i in range(1, num_elements+1):
        print(number, "×", i, "=", number * i)

    return 0


if __name__ == "__main__":
    main()
