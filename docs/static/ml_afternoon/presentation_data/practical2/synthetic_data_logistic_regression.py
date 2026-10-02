#!/usr/bin/env python3
"""
File to test logistic regression.
"""
from __future__ import print_function
import numpy as np
import argparse
from logistic_regression import gradient_descent
from scipy.special import expit
import matplotlib.pyplot as plt
import random


def parse_args(*argument_array):
    parser = argparse.ArgumentParser()
    parser.add_argument('--beta-star', nargs='+', action='append',
                        type=float, default=[-29, 0.06, 0.155])
    parser.add_argument('--num-points', type=int, default=20)
    args = parser.parse_args(*argument_array)
    return args


def d_dimensional_comparison(beta_star, num_points, l):
    d = len(beta_star) - 1
    X_list = [np.random.uniform(0, 256, num_points) for _ in range(d)]
    X = np.column_stack(X_list)
    X = np.column_stack((np.ones(num_points), X))

    distances = np.array([xi.dot(beta_star) for xi in X])
    Y = [1 if expit(dist) > random.random() else -1
         for dist in distances]

    x1_pos, x2_pos = zip(*[xi[1:] for xi, yi in zip(X, Y) if yi == 1])
    x1_neg, x2_neg = zip(*[xi[1:] for xi, yi in zip(X, Y) if yi == -1])

    plt.scatter(x1_pos, x2_pos, marker='+', color='red')
    plt.scatter(x1_neg, x2_neg, marker='o', color='blue')
    x2_star = decision(np.column_stack([np.ones(256), np.arange(256)]),
                       beta_star)
    beta_hat = gradient_descent(X, Y, l=l, epsilon=1e-8, step_size=1e-2,
                                max_steps=100)
    x2_hat = decision(np.column_stack([np.ones(256), np.arange(256)]),
                      beta_hat)
    plt.plot(np.arange(256), x2_star, color='purple')
    plt.plot(np.arange(256), x2_hat, color='green')
    plt.show()


def decision(x0x1, beta):
    """
    Given matrix of [x0, x1] values and beta, return corresponding
    x2 vector to draw decision boundary on x1-x2 plane.
    :param x0x1: data matrix (2 dimensional np.array), each row has length 2
    :param Y: response variables (1 dimensional np.array)
    :param x2: data vector (1 dimensional np.array)
    """
    # TODO: Implement
    return np.zeros(len(x0x1))

if __name__ == '__main__':
    args = parse_args()
    beta_star = args.beta_star
    d_dimensional_comparison(beta_star, args.num_points, l=1)
