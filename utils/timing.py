from functools import wraps
from statistics import mean
from time import perf_counter
from typing import Tuple, Any, Dict, List


def timed(runs: int):
    """
    This decorator serves to the execution time of the function it decorates returning a tuple with (result, time)

    :param runs: how many times the function should be ran
    :return:
    """

    def decorator(function: (Tuple[Any, ...], Dict[str, Any])) -> (Tuple[Any, ...], Dict[str, Any]):
        """

        :param function: function to be decorated
        :return: function
        """

        @wraps(function)
        def wrapper(*args: Tuple[Any], **kwargs: Dict[str, Any]) -> Tuple[Any, float]:
            """
            wrapper

            :param args: args
            :param kwargs: kwargs
            :return: (function result, time elapsed)
            """
            time: List[float] = []
            answer: Any = None

            for _ in range(runs):
                elapsed = perf_counter()
                answer = function(*args, **kwargs)
                time.append(perf_counter() - elapsed)

            return answer, mean(time)

        return wrapper

    return decorator

