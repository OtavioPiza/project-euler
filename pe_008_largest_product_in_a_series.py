from pe_000_utils import timed, print_answers
from functools import reduce

# == Project Euler: Problem 5 ======================================================================================== #
"""
The four adjacent digits in the 1000-digit number that have the greatest product are 9 × 9 × 8 × 9 = 5832.

73167176531330624919225119674426574742355349194934
96983520312774506326239578318016984801869478851843
85861560789112949495459501737958331952853208805511
12540698747158523863050715693290963295227443043557
66896648950445244523161731856403098711121722383113
62229893423380308135336276614282806444486645238749
30358907296290491560440772390713810515859307960866
70172427121883998797908792274921901699720888093776
65727333001053367881220235421809751254540594752243
52584907711670556013604839586446706324415722155397
53697817977846174064955149290862569321978468622482
83972241375657056057490261407972968652414535100474
82166370484403199890008895243450658541227588666881
16427171479924442928230863465674813919123162824586
17866458359124566529476545682848912883142607690042
24219022671055626321111109370544217506941658960408
07198403850962455444362981230987879927244284909188
84580156166097919133875499200524063689912560717606
05886116467109405077541002256983155200055935729725
71636269561882670428252483600823257530420752963450

Find the thirteen adjacent digits in the 1000-digit number that have the greatest product. What is the value of this
product?
"""

# == Common code ===================================================================================================== #

number = tuple(map(int, filter(lambda char: char.isnumeric(), '''
73167176531330624919225119674426574742355349194934
96983520312774506326239578318016984801869478851843
85861560789112949495459501737958331952853208805511
12540698747158523863050715693290963295227443043557
66896648950445244523161731856403098711121722383113
62229893423380308135336276614282806444486645238749
30358907296290491560440772390713810515859307960866
70172427121883998797908792274921901699720888093776
65727333001053367881220235421809751254540594752243
52584907711670556013604839586446706324415722155397
53697817977846174064955149290862569321978468622482
83972241375657056057490261407972968652414535100474
82166370484403199890008895243450658541227588666881
16427171479924442928230863465674813919123162824586
17866458359124566529476545682848912883142607690042
24219022671055626321111109370544217506941658960408
07198403850962455444362981230987879927244284909188
84580156166097919133875499200524063689912560717606
05886116467109405077541002256983155200055935729725
71636269561882670428252483600823257530420752963450
''')))

# == Solution 1 ====================================================================================================== #


@timed
def solution_1(series_size=13):
    """
    This solutions uses the fact that the next product in a series can be obtained by dividing the previous product by
    its first term and multiplying it by the term after its last. Moreover, this solutions takes in account that once a
    zero is found in a series, the number after it can become the next starting point since all products including it
    would result in zero.

    :param series_size:
    :return:
    """

    start_index = 0
    product = 1
    answer = 0
    new = True

    while start_index < len(number) - series_size:

        if new:
            new = False

            for index in range(start_index + series_size - 1, start_index - 1, -1):

                if number[index] == 0:
                    start_index = index
                    product = 1
                    new = True
                    break

                else:
                    product *= number[index]

        else:

            if number[start_index + series_size - 1] == 0:
                start_index = start_index + series_size - 1
                product = 1
                new = True

            else:
                product = number[start_index + series_size - 1] * product // number[start_index - 1]

        if product > answer:
            answer = product

        start_index += 1

    return answer

# == Solution 2 ====================================================================================================== #


@timed
def solution_2(series_size=13):
    answer = 0

    for start in range(0, len(number) - series_size):
        subset = number[start:start + series_size]
        product = reduce(lambda a, b: a * b, subset)

        if product > answer:
            answer = product

    return answer


if __name__ == '__main__':
    print_answers('Largest Product in a Series', solution_1, solution_2)
