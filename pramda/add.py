from typing import Callable, Union, overload

from .curry import curry

Numeric = Union[int, float]


@curry
def add(a: Numeric, b: Numeric) -> Numeric:
    return a + b
