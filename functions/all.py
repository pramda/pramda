from typing import Any, Callable
from functions.curry import curry
from functions.is_truthy import is_truethy


@curry
def all(func: Callable, targets: list[Any]) -> bool:
    result = True
    for t in targets:
        if not is_truethy(func(t)):
            result = False

    return result
