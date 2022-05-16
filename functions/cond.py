from typing import Any, Callable

from .curry import curry
from .is_truthy import is_truthy


@curry
def cond(pairs: list[tuple[Callable[[Any], bool], Callable[[Any], Any]]]) -> Callable:
    def inner(*args, **kwargs):
        for p in pairs:
            if len(p) != 2:
                continue

            if is_truthy(p[0](*args, **kwargs) if p[0].__code__.co_argcount > 0 else p[0]()):
                return p[1]()
        return None
    return inner
