import sys
import pytest
sys.path.append('./src/vrp/')
import vrp_train as vrp

class TestVrpTrain(object):
    def test_sum(self):
        # assert False
        actual = vrp.summation(1, 2)
        expected = 3
        assert actual == expected, "asdf"