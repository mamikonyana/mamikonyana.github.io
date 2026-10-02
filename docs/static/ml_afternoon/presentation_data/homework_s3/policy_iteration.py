#!/usr/bin/env python3
"""
Find optimal policy for the following problem:

Jack manages two locations for a nationwide car rental company.
Each day, some number of customers arrive at each location to rent
cars. If Jack has a car available, he rents it out and is credited
$10 by the national company. If he is out of cars at that location,
then the business is lost.  Cars become available for renting the
day after they are returned. To help ensure that cars are available
where they are needed, Jack can move them between the two locations
overnight, at a cost of $2 per car moved. We assume that the number
of cars requested and returned at each location are Poisson random
variables, meaning that the probability that the number is n is λ^n/n! e^{−λ},
where λ is the expected number.  Suppose λ is 3 and 4 for
rental requests at the first and second locations and 3 and 2 for
returns. To simplify the problem slightly, we assume that there can
be no more than 20 cars at each location (any additional cars are
returned to the nationwide company, and thus disappear from the
problem) and a maximum of five cars can be moved from one location
to the other in one night. We take the discount rate to be γ = 0.9
and formulate this as a continuing finite MDP, where the time steps
are days, the state is the number of cars at each location at the
end of the day, and the actions are the net numbers of cars moved
between the two locations overnight.
"""
import argparse
import itertools
from scipy.stats import poisson
from functools import lru_cache
import numpy as np

# Problem Constants
FIRST_RENTAL_MEAN = 3
SECOND_RENTAL_MEAN = 4

FIRST_RETURN_MEAN = 3
SECOND_RETURN_MEAN = 2


@lru_cache(maxsize=None)
def _poisson_pmf(k, mu):
    return poisson.pmf(k, mu)


def parse_args(*argument_array):
    parser = argparse.ArgumentParser()
    parser.add_argument('--discount-rate', type=float, default=0.9)
    parser.add_argument('--max-cars-per-location', type=int, default=10)
    parser.add_argument('--max-cars-can-move', type=int, default=4)
    parser.add_argument('--discounting-rate', type=float, default=0.9)
    args = parser.parse_args(*argument_array)
    return args


def p(new_state, reward, old_state, action):
    """
    Return p(new_state, reward | old_state, action)
    """
    COST_PER_CAR = 2
    return 0.


def greedy_policy(value, gamma, all_available_actions):
    policy = np.zeros(value.shape, dtype=np.int)
    # TODO: Implement
    return policy


def kd_range(arraylike):
    return itertools.product(*[range(element) for element in arraylike])


def main(args):
    all_available_actions = np.arange(-args.max_cars_can_move,
                                      1 + args.max_cars_can_move)
    policy = np.zeros((args.max_cars_per_location + 1,
                       args.max_cars_per_location + 1), dtype=np.int)
    value = np.zeros(policy.shape)
    for _iter in range(5):
        # TODO: Find the value function corresponding to the starting policy
        for i in range(5):
            value.dump('iter_{}-value_i{}.dat'.format(_iter, i))
        # TODO: Find the greedy policy that corresponds to the value function
        policy = greedy_policy(value, args.discounting_rate, all_available_actions)
        policy.dump('policy_{}.dat'.format(_iter))

    policy.dump('final_policy.dat')


if __name__ == '__main__':
    args = parse_args()
    main(args)


def test():
    assert p((3, 0), -6, (0, 0), -3) < 1e-9
