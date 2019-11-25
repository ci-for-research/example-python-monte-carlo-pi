#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for the ci_for_science module.
"""
import pytest

from ci_for_science import ci_for_science


def test_something():
    assert True


def test_with_error():
    with pytest.raises(ValueError):
        # Do something that raises a ValueError
        raise(ValueError)


# Fixture example
@pytest.fixture
def an_object():
    return {}


def test_ci_for_science(an_object):
    assert an_object == {}
