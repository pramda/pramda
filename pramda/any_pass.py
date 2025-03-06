from .curry import curry


@curry
def any_pass(preds, value):
    """
    any_pass takes a list of predicates and returns a predicate that returns True if at least one
    of the provided predicates is satisfied by the given value. The function returned is a
    curried function.

    Parameters:
    ----------
    preds : list[callable]
        A list of predicate functions. Each predicate should accept the same number of arguments.
    value : any
        The value to test against all predicates in `preds`.

    Returns:
    -------
    callable
        A curried predicate function. Returns True if at least one predicate is satisfied,
        False otherwise.

    Examples:
    ---------
    >>> is_even = lambda x: x % 2 == 0
    >>> is_positive = lambda x: x > 0
    >>> any_pass_pred = any_pass([is_even, is_positive])
    >>> any_pass_pred(2)  # True because 2 is even
    True
    >>> any_pass_pred(1)  # True because 1 is positive
    True
    >>> any_pass_pred(-2) # False because -2 is neither even nor positive
    False

    >>> is_divisible_by_3 = lambda x: x % 3 == 0
    >>> any_pass([is_even, is_divisible_by_3])(6) # True, 6 is even and divisible by 3
    True
    >>> any_pass([is_even, is_divisible_by_3])(2) # True, 2 is even
    True
    >>> any_pass([is_even, is_divisible_by_3])(5) # False, 5 is neither even nor divisible by 3
    False
    """
    return any(pred(value) for pred in preds)
