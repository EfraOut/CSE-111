"""Verify that the prefix and suffix functions work correctly."""

from words import *
import pytest


def test_prefix():
    """Verify that the prefix function works correctly.
    Parameters: none
    Return: nothing
    """
    assert prefix("", "") == ""
    assert prefix("", "correct") == ""
    assert prefix("clear", "") == ""
    assert prefix("happy", "funny") == ""
    assert prefix("cat", "catalog") == "cat"
    assert prefix("dogmatic", "dog") == "dog"
    assert prefix("jump", "joyous") == "j"
    assert prefix("unwise", "ungrateful") == "un"
    assert prefix("Disable", "dIstasteful") == "dis"


def test_suffix():
    """Verify that the suffix function works correctly.
    Parameters: none
    Return: nothing
    """
    assert suffix("", "") == ""
    assert suffix("", "correct") == ""
    assert suffix("clear", "") == ""
    assert suffix("happy", "funny") == "y"
    assert suffix("bed", "led") == "ed"
    assert suffix("television", "plain") == "n"
    assert suffix("distasteful", "ungrateful") == "teful"


# Call the main function that is part of pytest so that
# the test functions in this file will start executing.
pytest.main(["-v", "--tb=line", "-rN", __file__])
