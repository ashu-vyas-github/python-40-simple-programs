#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: ashutosh

Python program to find the smallest among three numbers

"""

import numpy


def main():

    print("Program to find the smallest number among given numbers\n")
    total_elements = int(input("How many numbers you wish to enter? "))
    print("Enter the numbers: ")
    all_numbers = numpy.zeros(total_elements)

    for idx in range(total_elements):
        num_in = float(input())
        all_numbers[idx] = num_in

    print("\nSmallest of all numbers: ", numpy.min(all_numbers))

    return 0


if __name__ == "__main__":
    main()