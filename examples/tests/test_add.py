from veritas import Integer
from veritas import given

def add(x: int, y: int) -> int:
    return x + y

@given(Integer(), Integer())
def test_adding(x: int, y: int) -> int:
    assert add(x, y) == x + y