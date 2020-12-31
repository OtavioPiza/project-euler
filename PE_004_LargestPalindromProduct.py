from PE_000_Utils import timed, print_answers

# == Project Euler: Problem 4 ==================================================================== #
"""
A palindromic number reads the same both ways. The largest palindrome made from the product of two
2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""

# == Solution 1 ================================================================================== #


@timed
def solution_1(lower_bound=100, upper_bound=999):
    """
    This method uses brute force to find the largest palindrome product of two numbers between 
    the lower and upper bound. To make this method more efficient we take advantage of the fact
    that all palindromes larger than 9 are multiples of 11.

    :param lower_bound: inclusive lower bound
    :param upper_bound: inclusive upper bound
    :return:
    """

    assert (9 < lower_bound < upper_bound)

    answer = -1

    def is_palindrome(number):
        return str(number)[::-1] == str(number)

    for a in range(upper_bound, lower_bound - 1, -1):

        for b in range(a - a % 11, lower_bound - 1, -11):   # Because all palindromes larger than
            # 9 are multiples of 11 we just need to check for products that contain it as a factor
            product = a * b

            if product > answer:    # Because the product is always decreasing as 'b' progresses,
                # once any product is lower than our current answer we can leave the loop safely

                if is_palindrome(product):
                    answer = product

            else:
                break

    return answer


if __name__ == '__main__':
    print_answers('Larges Palindrome Product', solution_1)
