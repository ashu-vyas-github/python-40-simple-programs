# -*- coding: utf-8 -*-
"""
@author: ashutosh

Program to onvert temperature units.

"""


def main():
    """
    The main function to execute upon call.

    Returns
    -------
    int
        returns integer 0 for safe executions.

    """

    print("Program to onvert temperature units.")

    celsius = float(input("Enter temperature in ℃: "))
    fahrenheit = (celsius * 9/5) + 32
    print('%.2f ℃ ≈ %0.2f ℉' % (celsius, fahrenheit))

    fahrenheit = float(input("Enter temperature in ℉: "))
    celsius = (fahrenheit - 32) * 5/9
    print('%.2f ℉ ≈ %0.2f ℃' % (fahrenheit, celsius))

    return 0


if __name__ == "__main__":
    main()
