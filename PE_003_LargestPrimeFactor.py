from math import sqrt
from time import time

# == Project Euler: Problem 3 ==================================================================== #
"""
What is the largest prime factor of the number 600851475143?
"""

# == Solution 1 ================================================================================== #


def solution_1(number=600851475143):
    """
    Brute force solution that uses domain restriction and prime factorization to reduce complexity

    -> Step 1: find a possible prime divisors to n between 2 and sqrt(n) + 1
    -> Step 2: if the divisor from step 1 evenly divides 'n' it becomes the answer and 'n' is
    divided by that number until no longer possible
    -> Step 3: print the answer

    :param number:
    :return:
    """

    time_elapsed = time()
    answer = -1

    """
    While not pretty, this is faster than using iter tools to include 2 in the tested range 
    bellow lowering the execution time on average by 4ms
    """
    if not number % 2:
        answer = 2

        while not number % 2:
            number /= 2

    for divisor in range(3, round(sqrt(number) + 1), 2):

        if not number % divisor:
            answer = divisor

            while not number % divisor:
                number /= divisor

    time_elapsed = (time() - time_elapsed) * 1000

    print(f'The answer is: {answer}')
    print(f'That took {time_elapsed}ms')


if __name__ == '__main__':
    print('Solution 1')
    solution_1()
