from typing import Any, Callable, ParamSpec, TypeVar, overload
from functions.curry import curry

P = ParamSpec('P')
T = TypeVar('T')


@overload
def adjust(index: int, func: Callable[P, T]) -> Callable[[list[Any]], T]:
    pass


@curry
def adjust(index: int, func: Callable[P, T], targets: list[Any]) -> T:
    return func(targets[index])
