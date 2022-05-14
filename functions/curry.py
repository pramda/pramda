from typing import Callable


def curry(func: Callable, left: int = None) -> Callable:
    if left is None:
        left = func.__code__.co_argcount

    def inner(*args, **kwargs):
        if len(args) >= left:
            return func(*args, **kwargs)

        def next(*received, **kwreceived):
            return func(*(args + received), **(kwargs.update(kwreceived) or {}))

        return next

    return inner
