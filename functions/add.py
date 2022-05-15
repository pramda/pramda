from typing import Callable, Union, overload

from .curry import curry

Numeric = Union[int, float]


@overload
def add(a: Numeric) -> Callable[[Numeric], Numeric]:
    pass


@curry
def add(a: Numeric, b: Numeric) -> Numeric:
    return a + b
