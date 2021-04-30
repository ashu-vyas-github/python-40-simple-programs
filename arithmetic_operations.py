# -*- coding: utf-8 -*-
"""
@author: ashutosh

Program to perform basic arithmetic operation with input from user.

"""


def arithmetic_operation():
    """
    Function to perform arithmetic operation

    Parameters
    ----------
    num1 : float
        First number.
    num2 : float
        Second number.
    operator : character
        Arithmetic operation character +, -, *, /.

    Returns
    -------
    result : float
        Result of arithmetic operation.

    """

    num1 = float(input("Enter First Number: "))
    num2 = float(input("Enter Second Number: "))

    print("\nWhich arithmetic operation would you like to perform?")
    ch = input("Select one of these operation +, -, *, /: ")

    result = 0
    if ch == '+':
        result = num1 + num2
    elif ch == '-':
        result = num1 - num2
    elif ch == '*':
        result = num1 * num2
    elif ch == '/':
        result = num1 / num2
    else:
        print("Input character is not recognized!")

    print()
    print(num1, ch, num2, "=", result)

    return 0


def main():
    """
    The main function to execute upon call.

    Returns
    -------
    int
        returns integer 0 for safe executions.

    """

    print("Program to perform basic arithmetic operation.\n")

    temp = arithmetic_operation()

    return 0


if __name__ == "__main__":
    main()
