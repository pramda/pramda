from .curry import curry


@curry
def all_pass(preds, value):
    """
    Parameters:
    ----------
    preds : list[callable]
        A list of predicate functions.  Each predicate should accept the same number of
        arguments.
    value : any
        The value to test against all predicates in `preds`.

    Returns:
    -------
    callable
        A curried predicate function that takes the arguments to test against all predicates
        in `preds`.  Returns True if all predicates are satisfied, False otherwise.

    Examples:
    ---------
    >>> is_even = lambda x: x % 2 == 0
    >>> is_positive = lambda x: x > 0
    >>> all_pass_pred = all_pass([is_even, is_positive])
    >>> all_pass_pred(2)  # True because 2 is even and positive
    True
    >>> all_pass_pred(1)  # False because 1 is not even
    False
    >>> all_pass_pred(-2) # False because -2 is not positive
    False


    >>> is_divisible_by_3 = lambda x: x % 3 == 0
    >>> all_pass([is_even, is_divisible_by_3])(6) #True, 6 is even and divisible by 3
    True
    >>> all_pass([is_even, is_divisible_by_3])(2) #False, 2 is even but not divisible by 3
    False

    Filepath:
    ---------
    """
    return all(pred(value) for pred in preds)
