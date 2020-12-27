from time import time

# == Project Euler: Problem 1 ==================================================================== #
"""
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
The sum of these multiples is 23. Find the sum of all the multiples of 3 or 5 below 1000.
"""

# == Solution 1 ================================================================================== #


def solution_1(upperbound=1000):
    time_elapsed = time()
    iterations = 0
    total = 0

    for number in range(3, upperbound):
        iterations += 1

        if number % 3 == 0 or number % 5 == 0:
            total += number

    time_elapsed = (time() - time_elapsed) * 1000

    print('Finished')
    print(f'That took {time_elapsed}ms and {iterations} iterations')
    print(f'The answer is: {total}')


# == Solution 2 ================================================================================== #


def solution_2(upperbound=1000):
    """
    Solution 1 refactored

    :param upperbound:
    :return:
    """

    time_elapsed = time()
    total = sum(filter(lambda number: not number % 3 or not number % 5, range(3, upperbound)))
    time_elapsed = (time() - time_elapsed) * 1000

    print('Finished')
    print(f'That took {time_elapsed}ms')
    print(f'The answer is: {total}')
