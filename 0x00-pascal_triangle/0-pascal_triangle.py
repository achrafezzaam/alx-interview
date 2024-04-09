#!/usr/bin/python3
''' Creating a Pascal Triangle for a given int '''


def pascal_triangle(n):
    ''' The Main function of the program.

    Args:
        n (int): The size of the Pascal Triangle
    Return: A list of lists of integers representing
            the Pascal Triangle of n.
    '''
    triangle = []
    if n > 0:
        for i in range(1, n + 1):
            row = []
            value = 1
            for j in range(1, i + 1):
                row.append(value)
                value = value * (i - j) // j
            triangle.append(row)
    return triangle
