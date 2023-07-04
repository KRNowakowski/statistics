import random
from scipy.stats import norm
from typing import Final


def generate_values(n : int, mean: int | float, std: int | float) -> [float]:
    """
    The function generates values consistent with normal distribution
    :param n: Number of elements
    :param mean: Arithmetic mean
    :param std: Standard deviation
    :return: A list with n elements that were generated for normal distribution
    """
    if n < 1:
        raise ValueError('The number of elements cannot be less than 1')

    if std < 0:
        raise ValueError('The standard deviation cannot be less than 0')

    values = list()
    for i in range(0, n):
        random_probability = random.uniform(0.0, 1.0)
        value = norm.ppf(random_probability, mean, std)
        values.append(value)
    return values


def main() -> None:
    MEAN: Final = 29
    STD: Final = 1.5
    print(generate_values(100, MEAN, STD))


if __name__ == '__main__':
    main()