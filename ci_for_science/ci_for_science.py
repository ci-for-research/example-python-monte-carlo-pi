"""Module to do some awesome scientific simulations."""

import argparse
import numpy as np
from compute_pi_cpp import compute_pi_cpp

__all__ = ["compute_pi"]

parser = argparse.ArgumentParser(
    description="run_simulation -n number_of_samples")
parser.add_argument('-n', '--number', required=True, type=int,
                    help="Number of samples")
parser.add_argument(
    '-m', '--mode', choices=["numpy", "cpp"], default="numpy")


def main():
    """Call an awesome scientific package."""
    # read the command line arguments
    args = parser.parse_args()
    samples = args.number
    mode = args.mode
    # perform the simulation
    print(f'Do some awesome science in {mode}!')
    if mode == "sequential":
        serial_pi = compute_pi(samples)
        print(f"Pi Serial calculation: {serial_pi:0.8f}")
    else:
        parallel_pi = compute_pi_cpp(samples)
        print(f"Pi parallel calculation: {parallel_pi:0.8f}")


def compute_pi(samples: int) -> float:
    """Compute the pi number using the Monte-Carlo method.

    Measure  the ratio between points that are inside a circle of radius 1
    and a square of size 1.
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


if __name__ == "__main__":
    main()
