from .lte import lte


def test_answer():
    assert lte(1, 2)
    assert lte(2, 2)
    assert not lte(2.1, 2)
    assert not lte(3, 2)
