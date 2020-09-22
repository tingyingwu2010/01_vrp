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
sys.path.append('./utils/')
import sm_functions as sm # type: ignore

def main():
    env = gym.make('vrp-v5')
    print(env.n_destinations)

def summation(a: int, b: int) -> int:
    return a + b

if __name__ == '__main__':
    main()