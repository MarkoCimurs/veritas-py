def add(x: int, y: int) -> int:
    return x + y

def test_adding_2_and_5():
    assert add(2, 5) == 7


def test_adding_2_and_6():
    assert add(2, 6) == 8