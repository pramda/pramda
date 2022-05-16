from .map import map
from .add import add


def _multiplication(a):
    return a * 2


def _uppercase(string):
    return string.upper()


def test_answer():
    assert map(_multiplication, [4, 2, 3]) == [8, 4, 6]
    assert map(_uppercase, ["a", "b", "c"]) == ["A", "B", "C"]
