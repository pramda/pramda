from typing import Union
from .curry import curry

Numeric = Union[int, float]


@curry
def lt(a: Numeric, b: Numeric) -> bool:
    return a < b
