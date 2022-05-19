from .gt import gt
from .filter import filter


def _is_even(n: int):
    return n % 2 == 0

def test_answer():
    assert filter(_is_even, [1, 2, 3, 4]) == [2, 4]
    assert filter(gt(1), [3, 50, 99]) == []