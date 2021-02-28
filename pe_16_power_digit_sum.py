from pe_000_utils import timed, print_answers
from functools import reduce

# == Project Euler: Problem 16 ======================================================================================= #
"""
215 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 21000?
"""

# == Solution 1 ====================================================================================================== #


@timed
def solution_1(power: int = 1000) -> int:
    return reduce(lambda a, b: int(a) + int(b), str(2 ** power))


if __name__ == "__main__":
    print_answers("Power Digit Sum", solution_1)
