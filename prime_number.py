# -*- coding: utf-8 -*-
"""
@author: ashutosh

A program to check prime number.

"""


def prime_number(num):

    if num > 1:  # prime number is always greater than 1
        for i in range(2, num):
            if (num % i) == 0:
                print(num, "is not a prime number")
                break
        else:
            print(num, "is a prime number")

    else:  # Number <= 1 is not prime number
        print(num, "is not a prime number")

    return 0


def main():
    """
    The main function to execute upon call.

    Returns
    -------
    int
        returns integer 0 for safe executions.

    """
    print("Program to check prime number.")

    # Taking input from user through prompt
    number = int(input("Enter any number: "))

    temp = prime_number(number)

    return 0


if __name__ == "__main__":
    main()
