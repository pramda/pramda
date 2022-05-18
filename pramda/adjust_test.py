from .adjust import adjust


def _inc(x: int) -> int:
    return x + 1


def test_answer():
    assert adjust(0, _inc, [1]) == 2
    assert adjust(0, _inc)([1]) == 2
    assert adjust(5, _inc)([1, 2, 3, 4, 5, 6]) == 7
