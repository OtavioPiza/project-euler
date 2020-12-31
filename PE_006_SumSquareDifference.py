from PE_000_Utils import timed, print_answers

# == Project Euler: Problem 6 ==================================================================== #
"""
Find the difference between the sum of the squares of the first one hundred natural numbers and the 
square of the sum.
"""


# == Solution 1 ================================================================================== #


@timed
def solution_1(upper_bound=101):
    """
    Calculates the difference between the square of the sum and the sum of the square

    :param upper_bound:
    :return:
    """

    return int((upper_bound - 1) * upper_bound / 2) ** 2 - sum(map(lambda number: number ** 2,
                                                                   range(upper_bound)))


if __name__ == '__main__':
    print_answers('Sum Square Difference', solution_1)
