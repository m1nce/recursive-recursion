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
    if (power == 0):
        return 1
    return base * exponent(base, power - 1)

print(exponent(2, 0))