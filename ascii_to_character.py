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

    ascii_val = int(input("Enter ASCII value to find character: "))

    print("\nASCII {asci} in character is \"{char}\""
          .format(asci=ascii_val, char=chr(ascii_val)))

    return 0


if __name__ == "__main__":
    main()
