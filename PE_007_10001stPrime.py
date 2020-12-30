from math import sqrt
from time import time

# == Project Euler: Problem 7 ==================================================================== #
"""
What is the 10 001st prime number?
"""

# == Solution 1 ================================================================================== #


def solution_1(index=10001):
    """
    This solutions uses the previous primes to more efficiently test for primality at the cost of
    memory

    :param index:
    :return:
    """
    assert index > 0 and type(index) == int

    time_elapsed = time()
    number = 1
    primes = [2]

    while len(primes) < index:
        number += 2
        is_prime = True
        divisor_upper_bound = round(sqrt(number) + 1)

        for divisor in primes:

            if divisor > divisor_upper_bound:
                break

            if not number % divisor:
                is_prime = False
                break

        if is_prime:
            primes.append(number)

    time_elapsed = (time() - time_elapsed) * 1000

    print(f'The answer is: {primes[-1]}')
    print(f'That took {time_elapsed}ms')


# == Solution 2 ================================================================================== #


def solution_2(index=10001):
    """
    This solution does not store previous primes to use them to check for primality and is thus
    slower albeit less memory hungry

    :param index:
    :return:
    """
    assert index > 1 and type(index) == int

    time_elapsed = time()
    primes_found = 1
    last_prime = 2
    number = 1

    while primes_found < index:
        number += 2
        is_prime = True
        divisor_upper_bound = round(sqrt(number) + 1)

        for divisor in range(3, divisor_upper_bound, 2):

            if not number % divisor:
                is_prime = False
                break

        if is_prime:
            primes_found += 1
            last_prime = number

    time_elapsed = (time() - time_elapsed) * 1000

    print(f'The answer is: {last_prime}')
    print(f'That took {time_elapsed}ms')


if __name__ == '__main__':
    print('Solution 1')
    solution_1(100000)

    print('Solution 2')
    solution_2(100000)
