from typing import Any, Callable, overload

from .curry import curry
from .is_truthy import is_truthy


@overload
def all(func: Callable[[Any], Any]) -> Callable[[list], bool]:
    pass


@curry
def all(func: Callable[[Any], Any], targets: list) -> bool:
    for t in targets:
        if not is_truthy(func(t)):
            return False
    return True
