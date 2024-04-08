#!/usr/bin/env python3
''' Creating a Pascal Triangle for a given int '''


def pascal_triangle(n):
    ''' The Main function of the program.

    Args:
        n (int): The size of the Pascal Triangle
    Return: A list of lists of integers representing
            the Pascal Triangle of n.
    '''
    if n <= 0:
        return []
    p_triangle = [[1]] * n
    for i in range(1, n):
        p_triangle[i] = row(p_triangle[i - 1], i+1)
    return p_triangle


def row(prev_row, n):
    ''' This function is responsible of creating the rows of
        the Pascal Triangle

    Args:
        prev_row (list): The previous row of the Triangle
        n (int)        : The row number
    Return: A list of integers representing the row n
            of the Pascal Triangle
    '''
    new_row = [1] * n
    for i in range(n):
        if i != 0 and i != (n - 1):
            new_row[i] = prev_row[i] + prev_row[i - 1]
    return new_row
