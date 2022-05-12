from typing import Callable, ParamSpec, TypeVar


T = TypeVar('T')
P = ParamSpec('P')


# TODO - pipe function
def pipe(*funcs: Callable[P, T]):
    def asdf(received):
        for func in funcs:
            func(received)
    return asdf
