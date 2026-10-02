#!/usr/bin/env python3
"""
This is a boilerplate file for you to get started on MNIST dataset.

This file has code to read labels and data from .gz files you can download from
http://yann.lecun.com/exdb/mnist/

Files will work if train-images-idx3-ubyte.gz file and
train-labels-idx1-ubyte.gz files are in the same directory as this
python file.
"""
from __future__ import print_function
import argparse
import gzip
import struct
import numpy as np
import matplotlib.pyplot as plt


def parse_args(*argument_array):
    parser = argparse.ArgumentParser()
    parser.add_argument('--mnist-train-data',
                        default='train-images-idx3-ubyte.gz',  # noqa
                        help='Path to train-images-idx3-ubyte.gz file '
                        'downloaded from http://yann.lecun.com/exdb/mnist/')
    parser.add_argument('--mnist-train-labels',
                        default='train-labels-idx1-ubyte.gz',  # noqa
                        help='Path to train-labels-idx1-ubyte.gz file '
                        'downloaded from http://yann.lecun.com/exdb/mnist/')
    args = parser.parse_args(*argument_array)
    return args


def main(args):
    # Read labels file into labels
    with gzip.open(args.mnist_train_labels, 'rb') as in_gzip:
        magic, num = struct.unpack('>II', in_gzip.read(8))
        all_labels = struct.unpack('>60000B', in_gzip.read(60000))

    # Read data file into numpy matrices
    with gzip.open(args.mnist_train_data, 'rb') as in_gzip:
        magic, num, rows, columns = struct.unpack('>IIII', in_gzip.read(16))
        all_data = [np.reshape(struct.unpack('>{}B'.format(rows * columns),
                                             in_gzip.read(rows * columns)),
                               (rows, columns))
                    for _ in range(60000)]

    # Select only labels and matrices of 4 and 9 digits.
    labels, data = zip(*[pair for pair in zip(all_labels, all_data)
                         if pair[0] in (4, 9)])

    # Select 42nd element and display to the user.
    plt.imshow(data[42], cmap='Greys')
    plt.title(str(labels[42]))
    plt.show()

if __name__ == '__main__':
  args = parse_args()
  main(args)
