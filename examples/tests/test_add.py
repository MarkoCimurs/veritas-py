from veritas import Integer
from veritas import given, settings, examples

def add(x: int, y: int) -> int:
    return x + y

@given(Integer(), Integer())
@settings(num_runs=10)
@examples((1, 2), (4, 5))
def test_adding(x: int, y: int) -> int:
    assert add(x, y) == x + y + 1