from matplotlib import pyplot as plt
from typing import Any, NoReturn, Tuple, List


def plot_range(params: Tuple[Tuple[Any], ...], functions: Tuple[(Any, )], x_label: str = 'input',
               x_axis_labeling_function: (Any) = lambda i: i[0]) -> NoReturn:
    """
    plots the time each function took to execute each of the provided parameters; if there are more then one parameters,
    the first one is used for the x-axis

    :param params: parameters for the functions
    :param functions: functions
    """
    x_axis: List[Any] = list(map(x_axis_labeling_function, params))
    y_axes: List[List[float]] = [[function(*param)[1] for param in params] for function in functions]
    index: int = 0

    for y_axis in y_axes:
        plt.plot(x_axis, y_axis, label=f'solution {(index := index + 1)}')

    plt.xlabel(x_label)
    plt.ylabel('time')
    plt.legend()
    plt.show()
