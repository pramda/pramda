from typing import Callable, overload, TypeVar
from functions import curry

T = TypeVar('T', int, float)


@overload
def add(a: T) -> Callable[[T], T]: pass


@curry
def add(a: T, b: T) -> T:
    return a + b
