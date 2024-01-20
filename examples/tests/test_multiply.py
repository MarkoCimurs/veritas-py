from veritas import Integer
from veritas import given, settings
import random

def multiply(x: int, y: int) -> int:
    return x * y

@settings(runs=3)
@given(Integer(), Integer())
def test_multiply_1(x: int, y: int) -> int:
    assert multiply(x, y) == x * y

@settings(runs=3)
@given(Integer(), Integer())
def test_multiply_2(x: int, y: int) -> int:
    result = multiply(x, y)
    if random.random() < 0.1:
        result += 1
    assert result == x * y