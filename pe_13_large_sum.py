from pe_000_utils import print_answers, timed

# == Project Euler: Problem 13 ======================================================================================= #
"""
Work out the first ten digits of the sum of the following one-hundred 50-digit numbers.
"""

# == Solution 1 ====================================================================================================== #


@timed
def solution_1(path: str = 'pe_13_large_sum.txt', limit: int = 10) -> str:

    with open(path, mode='r') as file:
        return str(sum(map(int, file.readlines())))[0:limit:]


if __name__ == '__main__':
    print_answers('Large Sum', solution_1)
