# -*- coding: utf-8 -*-
"""
@author: ashutosh

A program to count the number of each vowels in an input text.

"""


def letters_count():
    """
    Calculates number of times a letter (aeiou, alphabet) is repeated in a text.

    Returns
    -------
    None
        Displays the counts.

    """

    vowels = 'aeiou'  # string of vowels
    # english_letters = 'abcdefghijklmnopqrstuvwxyz'
    count = {}.fromkeys(vowels, 0)  # dictionary with each vowel a key, value=0

    input_text = input("Enter the text below:\n")  # input text
    input_text = input_text.casefold()  # make text case insensitive

    # count the vowels
    for char in input_text:
        if char in count:
            count[char] += 1

    print(count)

    return 0


def main():
    """
    The main function to execute upon call.

    Returns
    -------
    int
        returns integer 0 for safe executions.

    """

    print("Program to count the number of each vowels in an input text.\n")

    temp = letters_count()

    return 0


if __name__ == "__main__":
    main()
