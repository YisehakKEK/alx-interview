#!/usr/bin/python3
"""
Module for calculating the minimum number of operations to get n 'H' characters
"""

def minOperations(n):
    """
    Calculate the fewest number of operations needed to result in exactly n H characters.
    
    Only two operations are allowed:
    - Copy All
    - Paste

    Args:
        n (int): The target number of H characters

    Returns:
        int: Minimum number of operations or 0 if impossible
    """
    if n < 2:
        return 0

    operations = 0
    divisor = 2

    while n > 1:
        while n % divisor == 0:
            operations += divisor
            n //= divisor
        divisor += 1

    return operations
