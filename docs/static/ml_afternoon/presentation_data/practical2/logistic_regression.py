import numpy as np


def sigmoid(s):
    # TODO: Implement
    # You will find this function useful.
    return 0


def normalized_gradient(X, Y, beta, l):
    """
    :param X: data matrix (2 dimensional np.array)
    :param Y: response variables (1 dimensional np.array)
    :param beta: value of beta (1 dimensional np.array)
    :param l: regularization parameter lambda
    :return: normalized gradient, i.e. gradient normalized according to data
    """
    # TODO: Implement
    return np.zeros(X.shape[1])


def gradient_descent(X, Y, epsilon=1e-6, l=1, step_size=1e-4, max_steps=1000):
    """
    Implement gradient descent using full value of the gradient.
    :param X: data matrix (2 dimensional np.array)
    :param Y: response variables (1 dimensional np.array)
    :param l: regularization parameter lambda
    :param epsilon: approximation strength
    :param max_steps: maximum number of iterations before algorithm will
        terminate.
    :return: value of beta (1 dimensional np.array)
    """
    beta = np.zeros(X.shape[1])
    for s in range(max_steps):
        if s % 1000 == 0:
            print(s, beta)
        # TODO: Implement iterations.
    return beta
