from typing import List

from pe_000_utils import timed, print_answers

# == Project Euler: Problem 18 ======================================================================================= #
"""
By starting at the top of the triangle below and moving to adjacent numbers on the row below, the maximum total from top to bottom is 23.

3
7 4
2 4 6
8 5 9 3

That is, 3 + 7 + 4 + 9 = 23.
Find the maximum total from top to bottom of the triangle stored under pe_18_maximum_path_sum.txt
"""

# == Solution 1 ====================================================================================================== #


def get_triangle(path: str = 'pe_18_maximum_path_sum.txt') -> List[List[int]]:
    lines = []

    with open(path, mode='r') as file:

        while line := file.readline():
            lines.append(list(map(int, line.split(' '))))

    return lines


@timed
def solution_1(path: str = 'pe_18_maximum_path_sum.txt'):
    triangle = get_triangle(path)

    for i in range(len(triangle) - 2, -1, -1):

        for j in range(len(triangle[i])):

            if triangle[i + 1][j] > triangle[i + 1][j + 1]:
                triangle[i][j] += triangle[i + 1][j]

            else:
                triangle[i][j] += triangle[i + 1][j + 1]

    return triangle[0][0]


if __name__ == '__main__':
    print_answers('Maximum Path Sum', solution_1, params=('pe_18_maximum_path_sum.txt', ))
