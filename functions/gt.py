from typing import  Union
from functions.curry import curry

Numeric = Union[int, float]

@curry
def gt(a: Numeric, b: Numeric) -> bool:
    return a > b