# -*- coding: utf-8 -*-
"""17 ParamSpec：装饰器转发原函数参数签名

ParamSpec 同时捕获位置参数和关键字参数，使包装器保留被装饰函数的完整调用
契约。P.args 与 P.kwargs 只能在与该 ParamSpec 对应的转发位置使用。

若改用 Callable[..., R]，返回类型还能保留，但调用端的参数检查会丢失。
常见误区：只用 TypeVar 表示参数列表；TypeVar 只能表示一个类型。
"""
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
