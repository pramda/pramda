from typing import Callable,  TypeVar, overload
from functions.curry import curry

T = TypeVar('T')


@overload
def reduce(func: Callable[[T], T]) -> Callable[[list[T]], T]:
    pass


@curry
def reduce(func: Callable[[T], T], received: list[T]) -> T:
    def loop(before_result: T) -> T:
        if len(received) == 0:
            return before_result
        return loop(func(before_result, received.pop(0)))
    return loop(received.pop(0))
