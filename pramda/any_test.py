from .any import any


def is_one(x: int) -> bool:
    return x == 1


def test_answer():
    assert any(is_one, [1, 1, 1, 1])
    assert any(is_one, [1, 1, 1, 2])
    assert any(is_one, [2, 1, 1, 1])
    assert not any(is_one, [2, 2, 2, 2])
    assert any(is_one, [1.1, 1, 1, 1])
