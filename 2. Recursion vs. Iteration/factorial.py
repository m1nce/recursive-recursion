def factorial(integer):
    # base case
    if (integer == 1):
        return 1
    
    # recursive case
    return factorial(integer - 1) * integer


print(factorial(1))