import pytest


def always_returns_true():
    a = "hoku"
    print(a)
    return True


def test_always_returns_true():
    assert always_returns_true()
    
always_returns_true()
test_always_returns_true()
