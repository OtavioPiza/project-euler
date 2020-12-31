from math import sqrt
from PE_000_Utils import timed, print_answers

# == Project Euler: Problem 10 ======================================================================================= #
"""
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
Find the sum of all the primes below two million.
"""

# == Solution 1 ====================================================================================================== #


@timed
def solution_1(upper_bound=2000000):
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

    return sum(primes)


if __name__ == '__main__':
    print_answers('Summation Of Primes', solution_1)
