from typing import Union
from .curry import curry

Numeric = Union[int, float]


@curry
def gte(a: Numeric, b: Numeric) -> bool:
    return a >= b
