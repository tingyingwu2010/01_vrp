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

import gym

from vrp.envs.vrp_env import VRPEnv
sys.path.append('../../99_utilities/src')
import sm_functions as sm

def main():
    env = gym.make('vrp-v1')
    print('success!')


def summation(a: int, b: int) -> int:
    return a + b

if __name__ == '__main__':
    main()