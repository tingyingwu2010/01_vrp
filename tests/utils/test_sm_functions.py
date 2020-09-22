import random # type: ignore
import sys

import pytest
import numpy as np # type: ignore
import tensorflow as tf # type: ignore

import vrp.utils.sm_functions as sm # type: ignore

class TestSetSeed(object):
    def test_random_set_seed(self):
        sm.set_seed(123456789)
        random_actual = random.random()
        random_expected = 0.6414006161858726
       
        assert random_actual == random_expected, f"Expected: {random_expected}, got: {random_actual}"

    def test_np_set_seed(self):
        np_actual = np.random.random()
        np_expected = 0.532833024789759
        
        assert np_actual == np_expected, f"Expected: {np_expected}, got: {np_actual}"
        
    def test_tf_set_seed(self):
        tf_actual = tf.random.uniform(shape=[])
        tf_expected = 0.62868404
        
        assert tf_actual == tf_expected, f"Expected: {tf_expected}, got: {tf_actual}"

    def test_str(self):
        with pytest.raises(ValueError):
            sm.set_seed('hello world')