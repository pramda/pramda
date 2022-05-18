from typing import Callable, TypeVar

from .curry import curry

AT = TypeVar("AT")
RT = TypeVar("RT")


@curry
def reduce(func: Callable[[AT], AT], received: list[AT]) -> RT:
    def loop(before_result: AT) -> RT:
        if len(received) == 0:
            return before_result
        return loop(func(before_result, received.pop(0)))

    return loop(received.pop(0))
