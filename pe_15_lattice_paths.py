from pe_000_utils import print_answers, timed

# == Project Euler: Problem 15 ======================================================================================= #
"""
Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 
routes to the bottom right corner.

How many such routes are there through a 20×20 grid?
"""

# == Solution 1 ====================================================================================================== #
"""
They key to efficiently solving this problem is realizing that we can describe all the possible paths using only 'D' to
represent down and 'L' to represent left. Because on an n x n grid in which we must start at the top right and move to 
the bottom right, we will need to move left n times and right n times, we can obtain the total number of paths using
combinatorics: How many distinct ways are there to choose n out of 2n?
"""


@timed
def solution_1(grid_size: int = 20) -> int:
    total_paths = 1

    for i in range(grid_size):
        total_paths *= (2 * grid_size) - i
        total_paths //= i + 1

    return total_paths


# == Solution 2 ====================================================================================================== #
"""
We can also use dynamic programming, solving the problem in smaller parts by writing how many different routes there are
from any given point on the grid to the end. 
"""


@timed
def solution_2(grid_size: int = 20) -> int:
    grid_size += 1
    grid = [[0 if element != grid_size - 1 else 1 for element in range(grid_size)] for row in range(grid_size)]
    grid[-1] = list(map(lambda element: 1, grid[-1]))

    for i in range(grid_size - 2, -1, -1):
        for j in range(grid_size - 2, -1, -1):
            grid[i][j] = grid[i + 1][j] + grid[i][j + 1]

    return grid[0][0]


if __name__ == '__main__':
    print_answers("Lattice Paths", solution_1, solution_2, params=(20, ))
