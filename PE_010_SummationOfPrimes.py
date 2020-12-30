from math import sqrt
from time import time

# == Project Euler: Problem 10 ======================================================================================= #
"""
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
Find the sum of all the primes below two million.
"""

# == Solution 1 ====================================================================================================== #


def solution_1(upper_bound=2000000):
    time_elapsed = time()
    primes = [2]

    for number in range(3, upper_bound, 2):
        is_prime = True
        max_divisor = int(sqrt(number) + 1)

        for divisor in primes:

            if divisor > max_divisor:
                break

            if not number % divisor:
                is_prime = False
                break

        if is_prime:
            primes.append(number)

    answer = sum(primes)
    time_elapsed = (time() - time_elapsed) * 1000

    print(f'The answer is: {answer}')
    print(f'That took {time_elapsed}ms')


if __name__ == '__main__':
    print('Solution 1')
    solution_1()
