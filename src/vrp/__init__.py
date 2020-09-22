from vrp.envs.vrp_env_5 import VRPEnv5
from gym.envs.registration import register # type: ignore

register(
    id='vrp-v5',
    entry_point='vrp.envs:VRPEnv5'
)