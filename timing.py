from functools import wraps
from statistics import mean
from time import perf_counter
from typing import Tuple, Any, Dict, List


def timed(runs: int) -> int:
    """

    :param runs: how many times the function should be ran
    :return:
    """

    def decorator(function: (Tuple[Any, ...], Dict[str, Any])) -> (Tuple[Any, ...], Dict[str, Any]):
        """
        This decorator serves to the execution time of the function it decorates returning a tuple with (result, time)

        :param function: function to be decorated
        :return: function
        """

        @wraps(function)
        def wrapper(*args, **kwargs):
            """
            wrapper

            :param args:
            :param kwargs:
            :return: (function result, time elapsed)
            """
            times: List[float, ...] = []
            answer: Any = None

            for _ in range(runs):
                elapsed = perf_counter()
                answer = function(*args, **kwargs)
                times.append(perf_counter() - elapsed)

            return answer, mean(times)

        return wrapper

    return decorator

