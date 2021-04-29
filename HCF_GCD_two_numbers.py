# -*- coding: utf-8 -*-
"""
@author: ashutosh

Program to find the HCF using Euclidian algorithm.

"""


def compute_hcf_gcd(num1, num2):
    """
    Compute Highest Common Factor (HCF) aka Greatest Common Divisor (GCD).

    Parameters
    ----------
    num1 : float
        First number.
    num2 : float
        Second number.

    Returns
    -------
    num1 : float
        HCF or GCD of the two numbers.

    """
    while(num2):
        num1, num2 = num2, num1 % num2
    return num1


def main():
    """
    The main function to execute upon call.

    Returns
    -------
    int
        returns integer 0 for safe executions.

    """

    print("Program to find the HCF using Euclidian algorithm.")

    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    hcf_gcd = compute_hcf_gcd(num1, num2)

    print("\nHighest Common Factor, HCF = ", str(hcf_gcd))

    return 0


if __name__ == "__main__":
    main()
