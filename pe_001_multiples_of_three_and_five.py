from pe_000_utils import timed, print_answers

# == Project Euler: Problem 1 ==================================================================== #
"""
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
The sum of these multiples is 23. Find the sum of all the multiples of 3 or 5 below 1000.
"""

# == Solution 1 ================================================================================== #


@timed
def solution_1(upper_bound: int = 1000) -> int:
    total = 0

    for number in range(3, upper_bound):

        if number % 3 == 0 or number % 5 == 0:
            total += number

    return total

# == Solution 2 ================================================================================== #


@timed
def solution_2(upper_bound: int = 1000) -> int:
    """
    Solution 1 refactored

    :param upper_bound:
    :return:
    """

    return sum(filter(lambda number: not number % 3 or not number % 5, range(3, upper_bound)))


if __name__ == '__main__':
    print_answers('Multiples of Three and Five', solution_1, solution_2)
