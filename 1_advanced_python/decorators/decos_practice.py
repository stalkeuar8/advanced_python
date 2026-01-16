from typing import Callable
from functools import wraps

def silence_errors(func: Callable):
    def wrapper(*args, **kwargs):
        try:
            res = func(*args, **kwargs)
            return f"Result: {res}"
        except Exception as e:
            return e
    return wrapper

@silence_errors
def devider(num1: int, num2: int):
    return num1 / num2

# print(devider(1, 0))
# print(devider(0, 1))
# print(devider(6, 2))


def validate_positive(func: Callable):
    def wrapper(*args, **kwargs):
        for arg in args:
            if arg <= 0: raise ValueError("Must be positive")
        for kwarg in kwargs.values():
            if kwarg <= 0: raise ValueError("Must be positive")
        res = func(*args, **kwargs)
        return res
    return wrapper



def repeat(times: int = 1):
    def wrapper(func: Callable):
        @wraps(func)
        def inner(*args, **kwargs):
            res = None
            for i in range(1, times+1):
                res = func(*args, **kwargs)
            return res
        return inner
    return wrapper


def timer(limit: int):
    def wrapper(func: Callable):
        count = 0
        @wraps(func)
        def inner(*args, **kwargs):
            nonlocal count
            if count == limit:
                raise PermissionError("Limit reached.")
            count += 1
            return func(*args, **kwargs)
        return inner
    return wrapper



def memoize(func: Callable):
    cache = {}
    @wraps(func)
    def wrapper(*args):
        nonlocal cache
        if args in cache.keys():
            return cache[args]
        res = func(*args)
        cache[args] = res
        return res
    return wrapper