from time import time

# == Project Euler: Problem 6 ==================================================================== #
"""
Find the difference between the sum of the squares of the first one hundred natural numbers and the 
square of the sum.
"""


def solution_1(upper_bound=101):
    """
    Calculates the difference between the square of the sum and the sum of the square

    :param upper_bound:
    :return:
    """

    time_elapsed = time()
    answer = int((upper_bound - 1) * upper_bound / 2) ** 2 - sum(map(lambda number: number ** 2,
                                                                     range(upper_bound)))
    time_elapsed = (time() - time_elapsed) * 1000

    print(f'The answer is: {answer}')
    print(f'That took {time_elapsed}ms')
