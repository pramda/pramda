from .curry import curry
from .cond import cond


@curry
def _equal(a, b):
    return a == b


def _T(*_):
    return True


def _always(a):
    def inner(*_):
        return a

    return inner


def test_asnwer():
    a = cond([_equal(1), _always("a")], [_equal(100), _always("b")], [_T, _always("c")])
    assert a(1) == "a"
    assert a(100) == "b"
    assert a(1000) == "c"

    b = cond([_equal(1), _always("b")])
    assert b(1) == "b"
    assert b(10) is None
