from .curry import curry
from .pick import pick
from .omit import omit


@curry
def find(pred, arr):
    """
    Returns the first element of the list that satisfies the given predicate.

    Parameters:
    ----------
    pred : callable
        A function that takes an element as input and returns True if the element satisfies the condition,
        False otherwise.
    arr : list[any]
        The list to search in.

    Returns:
    -------
    any
        The first element that satisfies the predicate, or None if no such element exists.

    Examples:
    ---------
    >>> find(lambda x: x > 2, [1, 2, 3, 4])
    3
    >>> find(lambda x: x == 5, [1, 2, 3, 4])
    None

    Filepath:
    ---------
    """
    for element in arr:
        if pred(element):
            return element
    return None
