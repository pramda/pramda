from .cond import cond

def _equal(a):
    def inner(b):
        return a == b
    return inner

def _T():
    return True

def _always(a):
    def inner():
        return a
    return inner

def test_asnwer():
    a = cond([
        [_equal(1), _always("a")],
        [_equal(100), _always("b")],
        [_T, _always("c")]
    ])
    assert a(1) == "a"
    assert a(100) == "b"
    assert a(1000) == "c"

    b = cond([
        [_equal(1), _always("b")]
    ])
    assert b(1) == "b"
    assert b(10) == None