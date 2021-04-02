from typing import Tuple

from functools import wraps
from time import time


def timed(function):
    """
    This decorator serves to the execution time of the function it decorates

    :param function:
    :return:
    """

    @wraps(function)
    def run(*args, **kwargs):
        elapsed = time()

        answer = function(*args, **kwargs)
        time_elapsed = time() - elapsed

        print(f'The answer is: {answer}')
        print(f'That took {time_elapsed * 1000}ms')

    return run


def print_answers(name: str, *args: Tuple, params: Tuple = ()):
    """
    Prints the answer to a problem displaying its name and the execution time for each of the solutions provided

    :param name: name of the problem
    :param args: solutions (functions)
    :param params: parameters for the functions
    """

    print(f'Project Euler: {name}\n')

    for index in range(len(args)):
        print(f'-> Solution {index + 1}')
        args[index](*params)
        print()


def get_primes_eratosthenes_sieve():

    # TODO implement this
    return -1
