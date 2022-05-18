from .gte import gte


def test_answer():
    assert not gte(1, 2)
    assert gte(2, 2)
    assert gte(2.1, 2)
    assert gte(3, 2)
