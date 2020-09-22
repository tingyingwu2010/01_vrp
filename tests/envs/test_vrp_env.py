import gym

from vrp.envs.vrp_env import VRPEnv

class TestVrpEnv(object):
    
    def test_init(self):
        env = gym.make('vrp-v1')
        assert True