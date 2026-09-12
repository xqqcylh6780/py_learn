# -*- coding: utf-8 -*-
"""02 现代注解语法与运行时对象

Python 3.9+ 优先 list[int] / dict[str, int]；3.10+ 优先 X | Y；
Python 3.12+ 支持 PEP 695 的 type 语句和类型参数列表。
"""
from typing import get_args, get_origin

T1 = list[int]
T2 = dict[str, list[int]]
T3 = int | str
for t in (T1, T2, T3):
    print(t, 'origin=', get_origin(t), 'args=', get_args(t))

# 注解对象能在运行时被反射，但“可被反射”不等于“自动强制检查”。
def f(xs: list[int] | None) -> tuple[int, ...]:
    return tuple(xs or ())
print(f.__annotations__)
