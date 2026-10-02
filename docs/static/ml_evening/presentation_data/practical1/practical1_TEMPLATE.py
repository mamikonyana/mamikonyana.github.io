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
import getpass


def parse_args(*argument_array):
    parser = argparse.ArgumentParser()
    parser.set_defaults(function=main)
    parser.add_argument('--user', default=getpass.getuser(),
                        help='Override system username with something else to '
                             'be include in the output file.')
    subs = parser.add_subparsers()
    test_parser = subs.add_parser('test')
    test_parser.set_defaults(function=test_function_signatures)
    parser.add_argument('--csv', default='yerevan_april_9.csv.gz',
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
    poly_x = x
    return poly_x, y


def fit_ridge_regression(X, Y, l=0.1):
    """
    :param X: A numpy matrix, where each row is a data element (X)
    :param Y: A numpy vector of responses for each of the rows (y)
    :param l: ridge variable
    :return: A vector containing the hyperplane equation (beta)
    """
    D = X.shape[1]  # dimension + 1
    beta = np.zeros(D)  # FIXME: ridge regression formula.
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
    return featurize(apartment)


def my_beta():
    """
    :return: beta_hat that you estimate.
    """
    return np.zeros(1)


def main(args):
    df = pd.read_csv(args.csv)
    # TODO: Convert `df` into features (X) and responses (Y) using featurize
    beta = fit_ridge_regression(X, Y, l=0)
    # TODO you should probably create another function to pass to `cross_validate`
    scores = cross_validate(X, Y, fit_ridge_regression)
    print(np.mean(scores))


def test_function_signatures(args):
    apt = pd.Series({'price': 65000.0, 'condition': 'good', 'district': 'Center', 'max_floor': 9, 'street': 'Vardanants St', 'num_rooms': 3, 'region': 'Yerevan', 'area': 80.0, 'url': 'http://www.myrealty.am/en/item/24032/3-senyakanoc-bnakaran-vacharq-Yerevan-Center', 'num_bathrooms': 1, 'building_type': 'panel', 'floor': 4, 'ceiling_height': 2.7999999999999998})  # noqa
    x, y = my_featurize(apt)
    beta = my_beta()

    assert type(y) == float
    assert len(x.shape) == 1
    assert x.shape == beta.shape

if __name__ == '__main__':
    args = parse_args()
    args.function(args)
