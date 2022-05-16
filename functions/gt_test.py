from .gt import gt


def test_answer():
    assert not gt(1, 2)
    assert not gt(2, 2)
    assert gt(2.1, 2)
    assert gt(3, 2)
