#!/usr/bin/env python

import math

__author__ = "Minchan Kim"
__since__ = "June 23, 2023"

def sumPowersOf2(power):
    """
    Gets the sum of the first n powers of 2

    @param power: limit of the first n powers to sum
    @return: integer of sum of first n powers of 2
    ---
    >>> sumPowersOf2(3)
    14
    >>> sumPowersOf2(4)
    30
    >>> sumPowersOf2(1)
    2
    """
    if power == 1:
        return 2
    return (int) (math.pow(2, power) + sumPowersOf2(power - 1))