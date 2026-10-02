import numpy as np
from scipy.stats import multivariate_normal


def multi_normal_pdf(x, mean, covariance):
    """
    Evaluates Multivariate Gaussian Distribution density function
    :param x: location where to evaluate the density function
    :param mean: Center of the Gaussian Distribution
    :param covariance: Covariance of the Gaussian Distribution
    :return: density function evaluated at point x
    """
    var = multivariate_normal(mean=mean, cov=covariance)
    return var.pdf(x)


class GaussianMixtureModel(object):
    def __init__(self, num_mixtures):
        self.K = num_mixtures
        self.centers = []  # List of centers
        self.weights = []  # List of weights
        self.covariances = []  # List of covariances
        self.r = None  # Matrix of responsibilities, i.e. gamma

    def initialize(self, data):
        """
        :param data: data, numpy 2-D array
        """
        # TODO: Initialize cluster centers, weights, and covariances
        # Hint: Use K-means
        pass

    def fit(self, data, max_iter=100, precision=1e-6):
        """
        :param data: data to fit, numpy 2-D array
        """
        # TODO: Initialize Mixtures, then run EM algorithm until it converges.
        self.initialize(data)

        for iteration in range(1, max_iter + 1):
            # TODO: Perfor E step
            # TODO: Perfor M step
            # TODO: Check for termination
            continue

    def get_centers(self):
        return

    def get_covariances(self):
        return

    def get_weights(self):
        return

    def predict_cluster(self, data):
        """
        Return index of the clusters that each point is most likely to belong.
        :param data: data, numpy 2-D array
        :return: labels, numpy 1-D array
        """
        return None
