from veritas import Integer
from veritas import given, settings
import random

def multiply(x: int, y: int) -> int:
    return x * y

@given(Integer(), Integer())
def test_multiply_1(x: int, y: int) -> int:
    assert multiply(x, y) == x * y

