#!/usr/bin/env python

"""Tests for the ci_for_science module."""
from ci_for_science import compute_pi


def test_compute_pi():
    """Check that the computation approximates pi."""
    approx_pi = compute_pi(10000)

    predicate_1 = approx_pi < 3.15
    predicate_2 = approx_pi > 3.13

    assert predicate_1 and predicate_2
