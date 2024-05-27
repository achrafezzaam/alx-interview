#!/usr/bin/python3
''' Define the rotate_2d_matrix function '''


def rotate_2d_matrix(matrix):
    """ Rotate a given matrix 90 degrees clockwise

        Args:
            matrix [List[List]]: The 2D matrix to rotate

        Return:
            The same matrix rotate 90 degrees clockwise
    """
    size = len(matrix)
    for x in range(int(size/2)):
        for y in range(x, size - x - 1):
            save = matrix[x][y]
            matrix[x][y] = matrix[size - y - 1][x]
            matrix[size - y - 1][x] = matrix[size - x - 1][size - y - 1]
            matrix[size - x - 1][size - y - 1] = matrix[y][size - x - 1]
            matrix[y][size - x - 1] = save
    return matrix
