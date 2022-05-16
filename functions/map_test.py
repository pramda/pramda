from .map import map
from .add import add


def _multiplication(a, b):
    return a * b


def test_answer():
    assert map(add, [1, 2, 3]) == 6
    assert map(_multiplication, [4, 2, 3]) == 24
