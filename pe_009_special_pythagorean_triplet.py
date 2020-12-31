from pe_000_utils import timed, print_answers

# == Project Euler: Problem 9 ======================================================================================== #
"""
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
a^2 + b^2 = c^2

For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""

# == Solution 1 ====================================================================================================== #


@timed
def solution_1(abc_sum=1000):
    """
    This solution uses Euclid's formula to generate pythagorean triples

    a = m**2 - n**2
    b = 2mn
    c = m**2 + n**2

    m > n > 0, where m and n are integers

    Thus the sum of a, b, c is 2(m**2 + mn), once consequence of that is that no integer triplets exists with an odd sum

    :param abc_sum:
    :return:
    """
    assert not abc_sum % 2

    answer = -1
    current_sum = -1
    abc_sum //= 2
    m = 1

    while current_sum != abc_sum:
        m += 1
        current_sum = m**2

        """
        Because m is always increasing and the smallest sum for a given m is 2m(m + 1), if that exceeds what we are 
        looking for we can know for sure that no pythagorean triplet has required sum
        """
        if current_sum + m > abc_sum:
            break

        for n in range(1, m):
            current_sum += m*n  # this way we do not have to keep the operation m**2 unnecessarily

            if current_sum >= abc_sum:
                answer = (m**2 - n**2) * (2 * m * n) * (m**2 + n**2)
                break

            current_sum -= m*n  # this way we do not have to keep the operation m**2 unnecessarily

    return answer


if __name__ == '__main__':
    print_answers('Special Pythagorean Triplet', solution_1)
