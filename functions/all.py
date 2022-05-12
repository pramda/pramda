from typing import Any, Callable
from functions.curry import curry
from functions.is_truthy import is_truethy

@overload
def all(func: Callable[[Any], Any]) -> Callable[[list], bool]:
    pass

@curry
def all(func: Callable[[Any], Any], targets: list) -> bool:
    for t in targets:
        if not is_truethy(func(t)):
            return False
    return True
