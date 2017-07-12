import pytest
from pypackagelib import utils


def test_sum():
    num1 = 10
    num2 = 5
    res = utils.sum(num1, num2)
    assert(res == (num1 + num2))

def test_sub():
    num1 = 10
    num2 = 5
    res = utils.sub(num1, num2)
    assert(res == (num1 - num2))

def test_mul():
    num1 = 10
    num2 = 5
    res = utils.mul(num1, num2)
    assert(res == (num1 * num2))

def test_div():
    num1 = 10
    num2 = 5
    res = utils.div(num1, num2)
    assert(res == (num1 / num2))