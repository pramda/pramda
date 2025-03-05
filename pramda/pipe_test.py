from pramda import pipe


def _inc(x: int) -> int:
    return x + 1


def test_answer():
    assert (
        pipe(
            _inc,
            _inc,
            _inc,
            _inc,
            _inc,
        )(1)
        == 6
    )
