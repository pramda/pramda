from typing import Callable, TypeVar

from .curry import curry

AT = TypeVar("AT")


@curry
def filter(func: Callable[[AT], bool], arr: list[AT]) -> list[AT]:
    def loop(before_items, item, left_items):
        if len(left_items) == 0:
            return before_items + item
        return loop(
            before_items + item,
            [left_items[0]] if func(left_items[0]) else [],
            left_items[1:],
        )

    return loop([], [arr[0]] if func(arr[0]) else [], arr[1:])
