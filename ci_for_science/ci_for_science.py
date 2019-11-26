# -*- coding: utf-8 -*-
import logging

import numpy as np

__all__ = ["compute_pi"]

LOGGER = logging.getLogger(__name__)


def example():
    """Call an awesome scientific package."""
    LOGGER.info('Do some awesome science')
    print(compute_pi(100000))


def compute_pi(samples: int) -> float:
    """
    Compute the pi number using the Monte-Carlo method by measuring
    the ratio between points that are inside a circle of radius 1 and
    a square of size 1
    """
    # Take random x and y cartesian coordinates
    xs = np.random.uniform(size=samples)
    ys = np.random.uniform(size=samples)

    # Count the points inside the circle
    rs = np.sqrt(xs**2 + ys**2)
    inside = rs[rs < 1.0]

    # compute pi
    approx_pi = (float(inside.size) / samples) * 4

    return approx_pi
