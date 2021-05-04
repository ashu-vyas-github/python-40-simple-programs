# -*- coding: utf-8 -*-
"""
@author: ashutosh

Program to remove punctuations from input text.

"""


def remove_punctuations(punctuations=["'", "\"", "!", "(", ")", "-", "[", "]", "{", "}", ";", ":", "\\", "/", ",", "<", ">", ".", "?", "@", "#", "$", "%", "£", "`", "¦", "^", "&", "*", "_", "=", "~", "|", "¬"]):
    """
    Function to remove input punctuations from the given input text.

    Parameters
    ----------
    punctuations : list, optional
        Punctuations list to be filtered. The default is all punctuations on UK-Extended keyboard.

    Returns
    -------
    unpunctuated_text : string
        Filtered, unpunctuated string text.

    """

    input_text = input("Insert text with punctuations:\n")

    # remove punctuation from the string
    unpunctuated_text = ""
    for char in input_text:
        if char not in punctuations:
            unpunctuated_text = unpunctuated_text + char

    print(unpunctuated_text)  # display the unpunctuated string

    return 0


def main():
    """
    The main function to execute upon call.

    Returns
    -------
    int
        returns integer 0 for safe executions.

    """

    print("Program to remove punctuations from input text.\n")

    temp = remove_punctuations()

    return 0


if __name__ == "__main__":
    main()
