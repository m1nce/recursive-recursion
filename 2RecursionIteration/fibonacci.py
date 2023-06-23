#!/usr/bin/env python
__author__ = "Minchan Kim"
__since__ = "June 23, 2023"

# iterative fibonacci
"""
def fibonacci(index):
    a, b = 0, 1
    for i in range(index):
        a, b = b, a + b
    return a
"""

# recursive fibonacci
def fibonacci(index):
    # base case
    if index == 1 or index == 2:
        return 1
    
    # recursive case
    return fibonacci(index - 1) + fibonacci(index - 2)

# test cases
# print(fibonacci(6)) # returns 8
# print(fibonacci(10)) # returns 55