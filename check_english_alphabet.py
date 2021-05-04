# -*- coding: utf-8 -*-
"""
@author: ashutosh

Program to check if input character is in English alphabet or not.

"""


def english_alphabet_check():
    """
    Function to check if input character is in English alphabet or not.

    Parameters
    ----------
    character : char
        Input character to be checked.

    Returns
    -------
    character : char
        Whether an English character or not.

    """

    character = input("Enter a character: ")  # taking user input

    # Checking if the input is an alphabet
    if((character >= 'a' and character <= 'z') or (character >= 'A' and character <= 'Z')):
        print(character, "is in English alphabet.")
    else:
        print(character, "is not in English alphabet.")

    return 0


def main():
    """
    The main function to execute upon call.

    Returns
    -------
    int
        returns integer 0 for safe executions.

    """

    print("Program to check if input character is in English alphabet or not.")

    temp = english_alphabet_check()

    return 0


if __name__ == "__main__":
    main()
