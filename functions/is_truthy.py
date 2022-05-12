from typing import Any


def is_truethy(target: Any) -> bool:
    return (
        False
        if target in [False, '', 0, '0', None, [], {}] else
        True
    )
