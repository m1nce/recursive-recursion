#!/usr/bin/env python
__author__ = "Minchan Kim"
__since__ = "June 23, 2023"

def factorial(integer):
    # base case
    if (integer == 1):
        return 1
    
    # recursive case
    return factorial(integer - 1) * integer


print(factorial(1))