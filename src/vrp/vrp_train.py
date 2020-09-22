'''VRP with Deep Reinforcement Learning

The objective of this code is to reimplement the (Nazari et. al 2018) code
(both the environment and the agent).

Author: Stephen Mak
Date: 21/09/20

Version:
1. Initial Development
'''

import os
import sys

import gym # type: ignore

from vrp.envs.vrp_env_5 import VRPEnv5 # type: ignore
import vrp.utils.sm_functions as sm # type: ignore

def main() -> None:
    """Train agent on VRPEnv5

    TODO: Extended description + args + returns

    Args:
        big_table (int): An open Bigtable Table instance.
        keys (str): A sequence of strings representing the key of each table row
            to fetch.
        other_silly_variable (str): Another optional variable, that has a much
            longer name than the other args, and which does nothing.

    Returns:
        (Dict) A dict mapping keys to the corresponding table row data
        fetched. Each row is represented as a tuple of strings. For
        example:

        {'Serak': ('Rigel VII', 'Preparer'),
        'Zim': ('Irk', 'Invader'),
        'Lrrr': ('Omicron Persei 8', 'Emperor')}

        If a key from the keys argument is missing from the dictionary,
        then that row was not found in the table.

    Raises:
        IOError: An error occurred accessing the bigtable.Table object.
    """

    env = gym.make('vrp-v5')
    print(env.n_destinations)

def summation(a: int, b: int) -> int:
    return a + b

if __name__ == '__main__':
    main()