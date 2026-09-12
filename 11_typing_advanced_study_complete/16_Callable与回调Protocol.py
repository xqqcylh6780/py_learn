# -*- coding: utf-8 -*-
"""16 Callable 与回调 Protocol

简单签名可用 Callable；复杂签名（关键字名、重载、属性）通常用 Protocol 更准确。
"""
# 学习重点：Callable 表达位置参数和返回值，回调 Protocol 可表达关键字名等细节。
# - 简单函数参数优先 Callable[[Arg], Result]。
# - 调用约定包含关键字参数、属性或重载时，定义带 __call__ 的 Protocol。
# - 回调接口越窄，调用方越容易传入普通函数、对象或测试替身。
# 常见误区：只写 Callable[..., Any]，使回调的输入输出关系完全丢失。
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
