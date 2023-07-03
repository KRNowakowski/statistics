from scipy.stats import binom, beta


def calculate_binomial_distribution(n: int, p: float) -> {dict}:
    """
    The function determines the number of successes k in n trials with the probability of success p
    :param n: number of trials
    :param p: probability of success
    :return: the number of successes k in n trials with the probability of success p
    """

    probabilities = {}
    for k in range(n+1):
        probability = binom.pmf(k, n, p)
        probabilities[k] = probability
    return probabilities


def calculate_beta_distribution(p: float, a: int, b: int, reverse=False) -> float:
    """
    The function computes the probability of different base probabilities for an event with a successes and b failures
    :param p: success rate
    :param a: number of successes
    :param b: number of failures
    :param reverse: reverse = True means we want to calculate the opposite event
    :return: the probability of different base probabilities for an event with a successes and b failures
    """

    if reverse == True:
        return 1.0 - beta.cdf(p, a, b)

    return beta.cdf(p, a, b)


def main() -> None:
    print(calculate_binomial_distribution(2, 0.5))
    print(calculate_beta_distribution(.90, 1, 2))
    print(calculate_beta_distribution(.9, 8, 2) + calculate_beta_distribution(.9, 8, 2, True))


if __name__ == '__main__':
    main()

