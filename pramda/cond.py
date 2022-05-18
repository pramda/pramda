from typing import Callable

from .is_truthy import is_truthy


def cond(*pairs: list[Callable, Callable]) -> Callable:
    def inner(*args):
        def loop(left_pairs: list[list[Callable, Callable]]):
            if len(left_pairs) == 0:
                return None
            if is_truthy(left_pairs[0][0](*args)):
                return left_pairs[0][1](*args)
            return loop(left_pairs[1:])

        return loop(pairs)

    return inner
