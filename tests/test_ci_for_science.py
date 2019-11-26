#!/usr/bin/env python

"""Tests for the ci_for_science module."""
from ci_for_science import compute_pi


def test_compute_pi():
    """Check that the computation approximates pi."""
    approx_pi = compute_pi(100000)
    print("Approximate value of pi is: ", approx_pi)

    predicate_1 = approx_pi < 3.16
    predicate_2 = approx_pi > 3.12

    assert predicate_1 and predicate_2
