#!/usr/bin/env python3
"""
Kernel Density Estimator
"""
from __future__ import print_function
import argparse
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


class KDE(object):
    """
    use Epanechnikov kernel
    """
    def fit(self, data):
        """
        :param data: data to fit, numpy 2-D array
        """
        # TODO: Figure out what the bandwidth should be using
        # Gaussian Bandwidth Selector
        pass

    def log_density(self, data):
        """
        :param data: data to predict density for, numpy 2-D array
        :return: numpy 1-D array, with natural log density of each point
        provided.
        """
        # TODO: Evaluate and return log-densities
        pass


def parse_args(*argument_array):
    parser = argparse.ArgumentParser()
    parser.add_argument('--data', default='readings.csv')
    args = parser.parse_args(*argument_array)
    return args


def main(args):
    df = pd.read_csv(args.data)
    X = np.array(df[['reading']])
    plt.hist(X, bins=20)

    kde = KDE()
    kde.fit(X)
    # TODO: create a grid for plotting
    # TODO: calculate density of a grid
    # TODO: scale density so it matches the histogram
    # TODO: plot scaled density
    plt.tight_layout()
    plt.show()


if __name__ == '__main__':
    args = parse_args()
    main(args)
