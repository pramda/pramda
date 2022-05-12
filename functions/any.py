from typing import Callable, ParamSpec, TypeVar, overload
from functions import curry
from functions import is_truethy


P = ParamSpec('P')
T = TypeVar('T')


@overload
def any(func: Callable[P, T]) -> Callable[[list[P]], bool]:
    pass


@curry
def any(func: Callable[P, T], targets: list[P]) -> bool:
    result = False
    for t in targets:
        if is_truethy(func(t)):
            result = True

    return result
