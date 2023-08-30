from typing import Callable, Union, overload

from .curry import curry

Numeric = Union[int, float]


@curry
def dec(num: Numeric) -> Numeric:
    return num - 1
