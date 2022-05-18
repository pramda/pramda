from .lt import lt


def test_answer():
    assert lt(1, 2)
    assert not lt(2, 2)
    assert not lt(2.1, 2)
    assert not lt(3, 2)
