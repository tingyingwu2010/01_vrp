import sys
import pytest

import vrp.vrp_train as vrp # type: ignore

# class TestMain(object):
#     def test_main(self):
#         vrp.main()
#         assert 1

class TestVrpTrain(object):
    def test_sum(self):
        # assert False
        actual = vrp.summation(1, 2)
        expected = 3
        assert actual == expected, "asdf"