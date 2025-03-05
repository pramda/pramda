from pramda import reduce


def _add(a, b):
    return a + b


def _concat_string(a, b):
    return f"{a}{b}"


def test_answer():
    assert reduce(_add, [1, 2, 3]) == 6
    assert reduce(_concat_string, ["a", "b", "c"]) == "abc"
