#!/usr/bin/env python
__author__ = "Minchan Kim"
__since__ = "June 23, 2023"

def reverseString(word):
    """
    Reverses a string
    
    @param word: word to reverse
    @return: reversed word
    ---
    >>> reverseString('CAT')
    'TAC'
    >>> reverseString('RACECAR')
    'RACECAR'
    >>> reverseString('A')
    'A'
    >>> reverseString('')
    ''
    >>> reverseString('Hello')
    'olleH'
    """
    if len(word) == 0 or len(word) == 1:
        return word
    return word[-1] + reverseString(word[:-1])