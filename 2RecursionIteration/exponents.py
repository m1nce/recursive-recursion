#!/usr/bin/env python
__author__ = "Minchan Kim"
__since__ = "June 23, 2023"

# iterative exponent
"""
def exponent(base, power):
    sum = 1
    for i in range(power):
        sum *= base
    return sum
"""

# recursive exponent
def exponent(base, power):
    if power == 0:
        # base case
        return 1
    elif power % 2 == 0:
        # recursive case
        product = exponent(base, power / 2)
        return product * product
    else:
        # recursive case
        product = exponent(base, power // 2)
        return product * product * base

# print(exponent(2, 5)) # returns 32
print(exponent(17, 10)) # returns 201599390049