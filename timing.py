from typing import Tuple, Any, Dict
from functools import wraps
from time import perf_counter


def timed(function: (Tuple[Any, ...], Dict[str, Any])) -> (Tuple[Any, ...], Dict[str, Any]):
    """
    This decorator serves to the execution time of the function it decorates returning a tuple with (result, time)

    :param function: function to be decorated
    :return: function
    """

    @wraps(function)
    def run(*args, **kwargs):
        """
        wrapper

        :param args:
        :param kwargs:
        :return: (function result, time elapsed)
        """
        elapsed = perf_counter()
        answer = function(*args, **kwargs)
        return answer, perf_counter() - elapsed

    return run
