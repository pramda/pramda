from typing import Callable, TypeVar

from .curry import curry

AT = TypeVar("AT")
RT = TypeVar("RT")


@curry
def map(func: Callable[[AT], RT], arr: list[AT]) -> list[RT]:
    def loop(before_items, item, left_items):
        if len(left_items) == 0:
            return before_items + [item]
        return loop(before_items + [item], func(left_items[0]), left_items[1:])

    return loop([], func(arr[0]), arr[1:])
