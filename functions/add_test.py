from .add import add


def test_answer():
    assert add(1, 2) == 3
    assert add(1)(2) == 3
