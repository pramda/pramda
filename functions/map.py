from typing import Callable, List, TypeVar

from .curry import curry

AT = TypeVar("AT")
RT = TypeVar("RT")


@curry
def map(func: Callable[[AT], AT], arr: list[AT]) -> RT:
    def loop(before_result: AT) -> RT:
        if len(arr) == 0:
            return before_result
        return loop(func(before_result, arr.pop(0)))

    return loop(arr.pop(0))
