# -*- coding: utf-8 -*-
"""16 Callable 与回调 Protocol

简单签名可用 Callable；复杂签名（关键字名、重载、属性）通常用 Protocol 更准确。
"""
from collections.abc import Callable
from typing import Protocol

Unary = Callable[[int], int]
def apply(fn: Unary, value: int) -> int:
    return fn(value)

class Formatter(Protocol):
    def __call__(self, value: int, *, prefix: str = '') -> str: ...

def format_value(fn: Formatter, x: int) -> str:
    return fn(x, prefix='ID=')

print(apply(lambda x: x * 2, 5))
print(format_value(lambda value, *, prefix='': f'{prefix}{value}', 7))
