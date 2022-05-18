from typing import Any, Callable, overload

from .curry import curry
from .is_truthy import is_truthy


@curry
def any(func: Callable[[Any], Any], targets: list) -> bool:
    for t in targets:
        if is_truthy(func(t)):
            return True
    return False
