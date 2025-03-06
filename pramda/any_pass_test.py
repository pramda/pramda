from .any_pass import any_pass


def is_even(x):
    return x % 2 == 0


def is_positive(x):
    return x > 0


def is_divisible_by_3(x):
    return x % 3 == 0


def test_any_pass():
    any_pass_pred = any_pass([is_even, is_positive])
    assert any_pass_pred(2) is True
    assert any_pass_pred(1) is True
    assert any_pass_pred(-2) is True
    assert any_pass_pred(-1) is False
    assert any_pass([is_even, is_divisible_by_3])(6) is True
    assert any_pass([is_even, is_divisible_by_3])(2) is True
    assert any_pass([is_even, is_divisible_by_3])(5) is False
    assert any_pass([is_even, is_divisible_by_3])(0) is True
    assert any_pass([is_even, is_divisible_by_3])(3) is True
    assert any_pass([is_even, is_divisible_by_3])(-1) is False
    assert any_pass([], 1) is False
