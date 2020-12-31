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

        answer = function(*args, *kwargs)
        time_elapsed = time() - elapsed

        print(f'The answer is: {answer}')
        print(f'That took {time_elapsed * 1000}ms')

    return run
