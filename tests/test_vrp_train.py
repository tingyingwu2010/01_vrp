import sys
import pytest

import vrp.vrp_train as vrp # type: ignore


class TestVrpTrain(object):
    def test_sum(self):
        # assert False
        actual = vrp.summation(1, 2)
        expected = 3
        assert actual == expected, "asdf"