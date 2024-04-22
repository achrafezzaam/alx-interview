#!/usr/bin/python3
''' Define the minOperations function '''


def minOperations(n):
    ''' Compute the minimum number of operations necessary
        to achieve exactly n iterations of H

        Args:
            n (int): The desired result

        Return: The number of necessary operations. '''
    output = 0
    for i in range(n//2, 0, -1):
        if i == 0:
            return int(output + 1)
        if n % i == 0:
            return int(output + n / i + minOperations(i))

    return int(output)
