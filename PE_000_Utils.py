from functools import wraps
from time import time


def timed(function):

    @wraps(function)
    def run(*args, **kwargs):
        time_elapsed = time()

        answer = function(*args, *kwargs)
        time_elapsed = (time() - time_elapsed) * 1000

        print(f'The answer is: {answer}')
        print(f'That took {time_elapsed}ms')

    return run
