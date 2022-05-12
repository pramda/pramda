from typing import Callable, ParamSpec, TypeVar


T = TypeVar('T')
P = ParamSpec('P')


def curry(func: Callable[P, T], left: int = None) -> Callable[P, T] | T:
    if left == None:
        left = func.__code__.co_argcount

    def inner(*args: P.args, **kwargs: P.kwargs) -> T:
        if len(args) >= left:
            return func(*args, **kwargs)

        def next(*received, **kwreceived):
            return func(*(args + received), **(kwargs.update(kwreceived) or {}))
        return next

    return inner
