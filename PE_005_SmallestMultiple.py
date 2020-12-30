from functools import reduce
from math import sqrt
from time import time

# == Project Euler: Problem ====================================================================== #
"""
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any 
remainder. What is the smallest positive number that is evenly divisible by all of the numbers 
from 1 to 20?
"""

# == Solution 1 ================================================================================== #


def get_primes(upper_bound):
    """
    Generates a tuple with the primes up to the specified bound

    :param upper_bound: max possible prime non-inclusive
    :return: tuple with all the primes less than the upper bound
    """
    assert (upper_bound > 2)

    primes = [2]

    for number in range(3, upper_bound, 2):
        divisor_upper_bound = round(sqrt(number) + 1)
        is_prime = True

        for divisor in primes:

            if divisor > divisor_upper_bound:
                break

            if not number % divisor:
                is_prime = False
                break

        if is_prime:
            primes.append(number)

    return tuple(primes)


def solution_1(upper_bound=20):
    """
    This solutions first generates a list of all primes less than the upper bound and then
    iterates from 2 to upper_bound and storing the largest occurrence of a prime in each number in
    that range

    :param upper_bound:
    :return:
    """
    assert upper_bound > 2

    time_elapsed = time()
    primes = {}.fromkeys(get_primes(upper_bound), 0)

    for number in range(2, upper_bound):

        for divisor in primes.keys():
            total = 0

            while not number % divisor:
                total += 1
                number /= divisor

            if total > primes.get(divisor):
                primes[divisor] = total

    answer = reduce(lambda a, b: a * b, map(lambda item: item[0] ** item[1], primes.items()))
    time_elapsed = (time() - time_elapsed) * 1000

    print(f'The answer is: {answer}')
    print(f'That took {time_elapsed}ms')


if __name__ == '__main__':
    print('Solution 1')
    solution_1()
