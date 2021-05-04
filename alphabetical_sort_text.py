# -*- coding: utf-8 -*-
"""
@author: ashutosh

Program to alphabetically sort the words form input string.

Example:
    Input_text = split text into individual words
    Sorted_words = individual
                    into
                    split
                    text
                    words
"""


def alphabetical_sort():
    """
    Funcion to alphabetically sort words of string.

    Parameters
    ----------
    input_text : string
        Input text to be sorted.

    Returns
    -------
    sorted : string
        Sorted words of input string.

    """

    input_text = input("Enter a string:\n")

    words = input_text.split()  # split text into individual words

    words.sort()  # sort the list

    print("\nThe sorted words are:")
    for word in words:
        print(word)

    return 0


def main():
    """
    The main function to execute upon call.

    Returns
    -------
    int
        returns integer 0 for safe executions.

    """

    print("Program to alphabetically sort the words form input string.\n")

    temp = alphabetical_sort()

    return 0


if __name__ == "__main__":
    main()
