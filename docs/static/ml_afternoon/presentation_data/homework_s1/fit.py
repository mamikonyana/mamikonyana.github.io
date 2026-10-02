import pandas as pd
import numpy as np
from pystan import StanModel


def run_inference():
    df = pd.read_csv('3gaussians-10k.csv')
    X = np.array(df[['XX', 'YY']].values)
    K = 3

    data = {'D': 2,
            'K': 3,
            'N': 10000,
            'Omega0': np.identity(2),
            'alpha': K * [0.1],
            'beta0': 0.1,
            'dof0': 1.1,
            'm0': np.zeros(2),
            'x': X}

    model = StanModel(file='finite_gaussian_mixture.stan')

    return model.sampling(data=data, warmup=200, iter=700)


if __name__ == '__main__':
    sampling = run_inference()
    # TODO: Your code goes in here.
