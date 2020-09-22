import pytest
import gym # type: ignore
from vrp.envs.vrp_env_5 import VRPEnv5 # type: ignore

def summation(a: int, b: int) -> int:
    return a + b

class TestVrpEnv(object):
    
    @pytest.fixture
    def generate_env(self):
        '''Fixture that creates a random SupplierSelection Environment for
        a given seed. Usually use 123456789 (make sure to use a large number
        for the seed)'''
        def _make_env(seed):
            sm.random_seed(seed)
            env = gym.make('vrp-v5')
            return env
        return _make_env
    
    def test_init(self):
        env = gym.make('vrp-v5')
        assert True