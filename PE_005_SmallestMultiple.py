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


def solution_1(upper_bound=20):
    time_elapsed = time()

    def get_primes():
        primes = [2]

        for number in range(3, upper_bound, 2):
            max_divisor = round(sqrt(number) + 1)
            is_prime = True

            for divisor in primes:

                if not number % divisor:
                    is_prime = False
                    break;

                if divisor > max_divisor:
                    break

            if is_prime:
                primes.append(number)

        return tuple(primes)

    primes = {}.fromkeys(get_primes(), 0)

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

