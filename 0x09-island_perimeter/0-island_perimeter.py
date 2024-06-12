#!/usr/bin/python3
''' Define the island_perimeter function '''


def island_perimeter(grid):
    ''' Return the perimeter of an island discribed by a 2D list '''
    border = 0

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if (grid[i][j] == 1):
                if (i <= 0 or grid[i - 1][j] == 0):
                    border += 1
                if (i >= len(grid) - 1 or grid[i + 1][j] == 0):
                    border += 1
                if (j <= 0 or grid[i][j - 1] == 0):
                    border += 1
                if (j >= len(grid) - 1 or grid[i][j + 1] == 0):
                    border += 1
    return border
