from math import sqrt
from PE_000_Utils import timed, print_answers

# == Project Euler: Problem 7 ==================================================================== #
"""
What is the 10 001st prime number?
"""

# == Solution 1 ================================================================================== #


@timed
def solution_1(index=10001):
    """
    This solutions uses the previous primes to more efficiently test for primality at the cost of
    memory

    :param index:
    :return:
    """
    assert index > 0 and type(index) == int

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

    return primes[-1]

# == Solution 2 ================================================================================== #


@timed
def solution_2(index=10001):
    """
    This solution does not store previous primes to use them to check for primality and is thus
    slower albeit less memory hungry

    :param index:
    :return:
    """
    assert index > 1 and type(index) == int

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

    return last_prime


if __name__ == '__main__':
    print_answers('10001st Prime', solution_1, solution_2)
