# -*- coding: utf-8 -*-
"""17 ParamSpec：装饰器转发原函数参数签名"""
from collections.abc import Callable
from functools import wraps
from typing import ParamSpec, TypeVar

P = ParamSpec('P')
R = TypeVar('R')

def traced(fn: Callable[P, R]) -> Callable[P, R]:
    @wraps(fn)
    def wrapper(*args: P.args, **kwargs: P.kwargs) -> R:
        print('call', fn.__name__)
        return fn(*args, **kwargs)
    return wrapper

@traced
def add(a: int, b: int, *, scale: int = 1) -> int:
    return (a + b) * scale

print(add(2, 3, scale=10))
