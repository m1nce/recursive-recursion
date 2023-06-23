#!/usr/bin/env python
__author__ = "Minchan Kim"
__since__ = "June 23, 2023"

def triangle_number(number):
    """
    Returns the sum of the number and all integers before it until 0.

    @param number: number to find triangular number of
    @return: integer of trianglular number
    ---
    >>> triangle_number(3)
    6
    >>> triangle_number(4)
    10
    """
    # base case
    if number == 1:
        return 1
    # recursive case
    return number + triangle_number(number - 1)