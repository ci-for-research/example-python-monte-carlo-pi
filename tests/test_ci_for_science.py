#!/usr/bin/env python

"""Tests for the ci_for_science module."""
from ci_for_science import compute_pi
from compute_pi_cpp import compute_pi_cpp


def test_serial_pi():
    """Check the serial implentation."""
    call_montecarlo(compute_pi)


def test_parallel_pi():
    """Check the serial implentation."""
    call_montecarlo(compute_pi_cpp)


def call_montecarlo(function: callable, samples: int = 100000):
    """Check that the computation approximates pi."""
    approx_pi = function(100000)
    print("Approximate value of pi is: ", approx_pi)

    predicate_1 = approx_pi < 3.16
    predicate_2 = approx_pi > 3.12

    assert predicate_1 and predicate_2
