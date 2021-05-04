# -*- coding: utf-8 -*-
"""
@author: ashutosh

One line summary of the file

Explanation here. With 72 character liit.

"""
from datetime import datetime


def exponential_power_calculation(base, exponent=1.0):
    """
    Calculation of exponential power of number i.e. base^exponent.

    Parameters
    ----------
    base : float
        Base number.
    exponent : float, optional
        Exponent of the base. The default is 1.0.

    Returns
    -------
    value : float
        Value of the computation base^exponent.

    """
    value = base**exponent
    return value


def main():
    """
    The main function to execute upon call.

    Returns
    -------
    int
        returns integer 0 for safe executions.

    """

    print("Program to compare execution time of user-defined functions.")

    base = float(input("Enter value of base:"))
    exponent = float(input("Enter value of exponent:"))

    start_time = datetime.now()
    value = exponential_power_calculation(base, exponent)
    time_elapsed = datetime.now() - start_time

    print("\n{bse} raised to {exp} = {vle}".format(bse=base, exp=exponent, vle=value))
    print("\nTime elpased (hh:mm:ss.ms) {}".format(time_elapsed))

    return 0


if __name__ == "__main__":
    main()
