from vrp.envs.vrp_env import VRPEnv
from gym.envs.registration import register

register(
    id='vrp-v1',
    entry_point='vrp.envs:VRPEnv'
)