from .all_pass import all_pass


def is_even(x):
    return x % 2 == 0


def is_positive(x):
    return x > 0


def is_divisible_by_3(x):
    return x % 3 == 0


def test_all_pass():
    all_pass_pred = all_pass([is_even, is_positive])
    assert all_pass_pred(2) is True
    assert all_pass_pred(1) is False
    assert all_pass_pred(-2) is False
    assert all_pass([is_even, is_divisible_by_3])(6) is True
    assert all_pass([is_even, is_divisible_by_3])(2) is False
