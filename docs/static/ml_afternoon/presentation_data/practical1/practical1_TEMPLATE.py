#!/usr/bin/env python3
"""
Run regression on apartment data.
"""
from __future__ import print_function
import argparse
import pandas as pd
import numpy as np
import itertools
import matplotlib.pyplot as plt


def parse_args(*argument_array):
    parser = argparse.ArgumentParser()
    parser.add_argument('--csv',
                        help='CSV file with the apartment data.')
    args = parser.parse_args(*argument_array)
    return args


def featurize(apartment):
    """
    :param apartment: Apartment DataFrame row (a dictionary like object)
    :return: (x, y) tuple, where x is a numpy vector, and y is a number
    """
    return [1], apartment['price']


def poly_featurize(apartment, degree=2):
    """
    :param apartment: Apartment DataFrame row (a dictionary like object)
    :return: (x, y) tuple, where x is a numpy vector, and y is a number
    """
    x, y = featurize(apartment)
    poly_x = # TODO: use itertools.product to get higher degree elements.
    return poly_x, y


def fit_ridge_regression(X, Y, l=0.1):
    """
    :param X: A numpy matrix, where each row is a data element (X)
    :param Y: A numpy vector of responses for each of the rows (y)
    :param l: ridge variable
    :return: A vector containing the hyperplane equation (beta)
    """
    D = X.shape[1]  # dimension + 1
    beta = np.zeroes(D)  # FIXME: ridge regression formula.
    return beta


def cross_validate(X, Y, fitter, folds=5):
    """
    :param X: A numpy matrix, where each row is a data element (X)
    :param Y: A numpy vector of responses for each of the rows (y)
    :param fitter: A function that takes X, Y as parameters and returns beta
    :param folds: number of cross validation folds (parts)
    :return: list of corss-validation scores
    """
    scores = []
    # TODO: Divide X, Y into `folds` parts (e.g. 5)
    for i in range(folds):
        # TODO: train on the rest
        # TODO: Add corresponding score to scores
        pass
    return scores



def my_featurize(apartment):
    """
    This is the function we will use for scoring your implmentation.
    :param apartment: apartment row
    :return: (x, y) pair where x is feature vector, y is the response variable.
    """
    return x, y


def my_beta():
    """
    :return: beta_hat that you estimate.
    """
    return np.zeroes(1)


def main(args):
    df = pd.read_csv(args.csv)
    # TODO: Convert `df` into features (X) and responses (Y) using featurize
    beta = fit_ridge_regression(X, Y, l=0)
    # TODO you should probably create another function to pass to `cross_validate`
    scores = cross_validate(X, Y, fit_ridge_regression)
    print(np.mean(scores))


if __name__ == '__main__':
    args = parse_args()
    main(args)
