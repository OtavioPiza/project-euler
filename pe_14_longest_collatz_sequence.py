from pe_000_utils import print_answers, timed

# == Project Euler: Problem 14 ======================================================================================= #
"""
The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:
13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1

It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved
yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
"""

# == Solution 1 ====================================================================================================== #


def get_next_number(number: int) -> int:
    return number / 2 if not number % 2 else number * 3 + 1


@timed
def solution_1(upper_limit: int = 1000000) -> int:
    longest = -1
    sequences = {-1: -1}

    for number in range(1, upper_limit, 2):
        current = number
        length = 1

        while current != 1:

            if current in sequences.keys():
                length += sequences[current] - 1
                break

            length += 1
            current = get_next_number(current)

        sequences[number] = length
        if length > sequences[longest]:
            longest = number

    return longest


if __name__ == '__main__':
    print_answers('Longest Collatz Sequence', solution_1)
