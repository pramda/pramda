from typing import Callable, overload, TypeVar
from functions.curry import curry

AT = TypeVar('AT')
RT = TypeVar('RT')

@overload
def adjust(index: int, func: Callable) -> Callable[[list], RT]:
    pass


@curry
def adjust(index: int, func: Callable[[AT], RT], targets: list[AT]) -> RT:
    return func(targets[index])
