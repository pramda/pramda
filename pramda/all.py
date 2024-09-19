from typing import Any, Callable, overload

from .curry import curry
from .is_truthy import is_truthy


"""
Returns True if all elements of the list match the predicate, False otherwise.

Example:
```python
from pramda import all

is_one = lambda x: x == 1

all(is_one, [1, 1, 1, 1])   # True
all(is_one, [1, 1, 1, 2])   # False
all(is_one)([2, 1, 1, 1])   # False
all(is_one)([2, 2, 2, 2])   # False
all(is_one)([1, 1, 1, 1])   # True
```
"""


@curry
def all(func: Callable[[Any], Any], targets: list) -> bool:
    for t in targets:
        if not is_truthy(func(t)):
            return False
    return True
