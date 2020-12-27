from time import time

# == Project Euler: Problem 4 ==================================================================== #
"""
A palindromic number reads the same both ways. The largest palindrome made from the product of two
2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""

# == Solution 1 ================================================================================== #


def solution_1(lower_bound=100, upper_bound=999):
    time_elapsed = time()
    answer = -1

    def is_palindrome(number):
        return str(number)[::-1] == str(number)

    for a in range(upper_bound, lower_bound - 1, -1):

        for b in range(a - a % 11, lower_bound - 1, -11):
            product = a * b

            if product > answer:

                if is_palindrome(product):

                    answer = product

            else:
                break

    time_elapsed = (time() - time_elapsed) * 1000

    print(f'The answer is: {answer}')
    print(f'That took {time_elapsed}ms')


