#!/usr/bin/python3
'''
File: 0-island_perimeter.py
'''


def island_perimeter(grid):
    '''
    Calculates the perimeter of the island described in the grid.
    '''
    perimeter = 0
    rows = len(grid)
    cols = len(grid[0])

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                perimeter += 4  # assumption that all sides are exposed
                # Check adjacent cells and subtract the shared sides
                if i > 0 and grid[i - 1][j] == 1:
                    perimeter -= 2
                if j > 0 and grid[i][j - 1] == 1:
                    perimeter -= 2
    return perimeter
