import logging

from .ci_for_science import compute_pi

logging.getLogger(__name__).addHandler(logging.NullHandler())

__author__ = "Felipe Zapata"
__email__ = 'f.zapata@esciencecenter.nl'

__all__ = ["compute_pi"]
