from typing import Callable


def pipe(*funcs_tuple: Callable) -> Callable:
    funcs = list(funcs_tuple)

    def loop(*args):
        if len(funcs) == 1:
            return funcs.pop(0)(*args)
        return loop(funcs.pop(0)(*args))

    return loop
