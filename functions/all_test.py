from .all import all


def is_one(x: int) -> bool:
    return x == 1


def test_answer():
    assert all(is_one, [1, 1, 1, 1])
    assert not all(is_one, [1, 1, 1, 2])
    assert not all(is_one, [2, 1, 1, 1])
    assert not all(is_one, [2, 2, 2, 2])
    assert not all(is_one, [1.1, 1, 1, 1])
