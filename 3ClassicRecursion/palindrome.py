def isPalindrome(word):
    """
    Indicates if word is a palindrome
    
    @param word: word to check if it is a palindrome
    @return: palindrome (T/F)
    ---
    >>> isPalindrome('racecar')
    True
    >>> isPalindrome('flower')
    False
    >>> isPalindrome('Kayak')
    True
    >>> isPalindrome('High')
    False
    >>> isPalindrome('hh')
    True
    """
    word = word.lower()
    if len(word) == 0:
        return True
    elif word[0] != word[-1]:
        return False
    return isPalindrome(word[1:-1])