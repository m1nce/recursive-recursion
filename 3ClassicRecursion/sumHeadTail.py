#!/usr/bin/env python
__author__ = "Minchan Kim"
__since__ = "June 23, 2023"

def sumHeadTail(numbers):
    """
    Returns the sum of an array
    
    @param numbers: list of numbers
    @return: integer representing sum of array
    ---
    >>> sumHeadTail([1, 2, 3, 4, 5])
    15
    >>> sumHeadTail([5])
    5
    >>> sumHeadTail([])
    0
    """
    if len(numbers) == 0:
        return 0
    return numbers[0] + sumHeadTail(numbers[1:])