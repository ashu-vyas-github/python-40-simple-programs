# -*- coding: utf-8 -*-
"""
@author: ashutosh

Program to find the character from an input ASCII value.

Example: "97" in ASCII is character "a"

"""


def main():
    """
    The main function to execute upon call.

    Returns
    -------
    int
        returns integer 0 for safe executions.

    """

    print("Program to find the character from an input ASCII value.")

    ascii_in_numeric = int(input("Enter ASCII value to find character: "))

    print("\nASCII {num} in character is \"{asci}\""
          .format(num=ascii_in_numeric, asci=chr(ascii_in_numeric)))

    return 0


if __name__ == "__main__":
    main()
