import numpy as np


def random_initialize(data_array, num_clusters):
    # TODO: Initialize cluster centers by sampling `num_clusters` points
    # uniformly from data_array.
    return list()


def plus_plus_initialize(data_array, num_clusters):
    # TODO: Initialize cluster centers using k-means++ algorithm.
    return list()


class KMeans(object):
    def __init__(self, num_mixtures):
        self.K = num_mixtures
        self.mus = []

    def initialize(self):
        # TODO: Initialize cluster centers
        # Hint: Use one of the function at the top of the file.
        pass

    def fit(self, data):
        """
        :param data: data to fit, numpy 2-D array
        """
        # TODO: Initialize Mixtures, then run EM algorithm until it converges.
        pass

    def predict(self, data):
        """
        Return index of the cluster the point is most likely to belong.
        :param data: data, numpy 2-D array
        :return: labels, numpy 1-D array
        """
        pass

    def get_centers(self):
        return list(zip(self.centers, self.covs))
