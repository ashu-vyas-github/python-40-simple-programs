#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: ashutosh

This is a simple program to convert kilometres to miles, or miles to kilometres

"""
def main():

    print("Program to convert distance units\n")
    print("1. Kilometres to Miles")
    print("2. Miles to Kilometres")
    option = int(input("Select the distance conversion 1 or 2: "))

    if option == 1:
        ratio = 0.632137 # 1km = 0.632 miles
        kilometres = float(input("Enter distance in Kilometres: "))
        miles = kilometres * ratio
        print("Distance in Miles: ", str(miles), " miles")
    elif option == 2:
        ratio = 1.609344 # 1ml = 1.61 kms
        miles = float(input("Enter distance in Miles: "))
        kilometres = miles * ratio
        print("Distance in Kilometres: ", str(kilometres), " kms")
    else:
        print("\nPlease select correct option: 1 or 2\n")
        main()

    return 0


if __name__ == "__main__":
    main()
