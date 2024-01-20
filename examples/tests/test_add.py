from veritas import Integer, Lists
from veritas import given, settings, examples

def add(x: int, y: int) -> int:
    return x + y

@given(Integer(), Integer())
@settings(num_runs=10)
@examples((1, 2), (4, 5))
def test_adding(x: int, y: int) -> int:
    assert add(x, y) == x + y


@given(Lists(Integer(min_value=0, max_value=10), min_length=0, max_length=3))
@settings(num_runs=3)
@examples([[1,2,3]], [ [4, 4, 4]])
def test_list_generation(xs):
    print(xs)
    assert True