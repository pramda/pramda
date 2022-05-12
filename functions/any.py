from typing import Any, Callable, overload
from functions import curry
from functions import is_truethy



@overload
def any(func: Callable[[Any], Any]) -> Callable[[list], bool]:
    pass


@curry
def any(func: Callable[[Any], Any], targets: list) -> bool:
    for t in targets:
        if is_truethy(func(t)):
            return True 
    return False
