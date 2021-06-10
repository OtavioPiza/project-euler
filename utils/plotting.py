from matplotlib import pyplot as plt
from typing import Any, NoReturn, Tuple, List
from concurrent.futures import ThreadPoolExecutor


def plot_range(params: Tuple[Tuple[Any], ...], functions: Tuple[(Any, )]) -> NoReturn:
    x_axis: List[Any, ...] = list(map(lambda i: i[0], params))
    y_axes: List[List[float, ...]] = [[function(*param)[1] for param in params] for function in functions]
    print(y_axes)
    index: int = 0

    for y_axis in y_axes:
        plt.plot(x_axis, y_axis, label=f'line {(index := index + 1)}')

    plt.legend()
    plt.show()
