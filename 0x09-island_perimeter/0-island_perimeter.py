#!/usr/bin/python3
"""Island Perimeter
"""


def island_perimeter(grid):
    """returns the perimeter of the island described in grid

    grid: a list of list of integers

    return: perimeter of the island described in grid
    """

    perimeter = 0

    # Loop through each row of the grid
    for row in grid:
        # Loop through each cell in the row
        for cell in row:
            if cell == 1:  # If it's land
                perimeter += 4  # Count all four sides

                # Check if there's land in the adjacent cells
                # Subtract 1 for each adjacent land cell
                c_index = row.index(cell)
                r_index = grid.index(row)
                if c_index > 0 and row[c_index - 1] == 1:
                    perimeter -= 1
                if c_index < len(row) - 1 and row[c_index + 1] == 1:
                    perimeter -= 1
                if r_index > 0 and grid[r_index - 1][c_index] == 1:
                    perimeter -= 1
                if r_index < len(grid) - 1 and grid[r_index + 1][c_index] == 1:
                    perimeter -= 1

    return perimeter
