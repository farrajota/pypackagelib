import pytest
import pypackagelib


def test_sum():
    num1 = 10
    num2 = 5
    res = pypackagelib.utils.sum(num1, num2)
    assert(res == (num1 + num2))

def test_sub():
    num1 = 10
    num2 = 5
    res = pypackagelib.utils.sub(num1, num2)
    assert(res == (num1 - num2))

def test_mul():
    num1 = 10
    num2 = 5
    res = pypackagelib.utils.mul(num1, num2)
    assert(res == (num1 * num2))

def test_div():
    num1 = 10
    num2 = 5
    res = pypackagelib.utils.div(num1, num2)
    assert(res == (num1 / num2))