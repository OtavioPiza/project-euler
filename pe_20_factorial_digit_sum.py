from pe_000_utils import timed, print_answers
from functools import reduce

# == Project Euler: 20 =============================================================================================== #
"""
n! means n × (n − 1) × ... × 3 × 2 × 1

For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100!
"""

# == Solution 1 ====================================================================================================== #


@timed
def solution_1(number: int = 100) -> int:
    return reduce(lambda a, b: int(a) + int(b), str(reduce(lambda a, b: a * b, range(1, number + 1))))


if __name__ == '__main__':
    print_answers('Factorial Digit Sum', solution_1)
