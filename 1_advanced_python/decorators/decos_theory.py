from typing import Callable, Coroutine
import time
from functools import wraps

def limiter(limit: int):
    def wrapper(func: Callable | Coroutine):
        @wraps(func)
        def inner(*args, **kwargs):
            nonlocal limit
            if limit == 0:
                raise Exception("Limit reached.")
            start = time.time()
            res = func(*args, **kwargs)
            end = time.time()
            print(f"Time: {end-start}")
            limit -= 1
            return res
        return inner

    return wrapper

@limiter(2)
def my_func(num):
    return num

try:
    print(my_func(5))
except Exception as e:
    print(e)






def logger(func: Callable):
    def wrapper(*args, **kwargs):
        print(f"Func '{func.__name__}' | args: '{args if len(args) > 0 else 'No args'}' | kwargs: '{kwargs if len(kwargs) > 0 else 'No kwargs'}'")
        res = func(*args, **kwargs)
        return res
    return wrapper

@logger
def my_func(a: int = 1, b: int = 3, c: int = 5):
    return f"Result: {a + b + c}"

print(my_func())
print(my_func(a=1, b=3, c=5))
print(my_func(1, 3, c=5))













