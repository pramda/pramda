from typing import Any, Callable, overload

from .curry import curry
from .is_truthy import is_truthy


@curry
def all(func: Callable[[Any], Any], targets: list) -> bool:
    for t in targets:
        if not is_truthy(func(t)):
            return False
    return True
