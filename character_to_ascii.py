# -*- coding: utf-8 -*-
"""
@author: ashutosh

Program to find the ASCII value of a character.

Example: Character "c" has ASCII value as 99

"""


def main():
    """
    The main function to execute upon call.

    Returns
    -------
    int
        returns integer 0 for safe executions.

    """

    print("Program to find the ASCII value of a character.")

    character_input = input("Enter any single character: ")

    print("\nCharacter \"{char}\" has ASCII value {asci}"
          .format(char=character_input, asci=ord(character_input)))

    return 0


if __name__ == "__main__":
    main()
