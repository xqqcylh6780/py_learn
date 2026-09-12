# -*- coding: utf-8 -*-
"""02 现代注解语法与运行时对象

Python 3.9+ 优先 list[int] / dict[str, int]；3.10+ 优先 X | Y；
Python 3.12+ 支持 PEP 695 的 type 语句和类型参数列表。
"""
# 学习重点：现代语法让类型关系更直接，但最低 Python 版本决定能否解析。
# - list[int] 是参数化泛型，X | Y 是联合类型。
# - get_origin() 可取得外层容器，get_args() 可取得内部类型参数。
# - 库代码升级语法前要先确认用户环境和类型检查器版本。
# 常见误区：认为参数化注解能直接用于所有 isinstance() 检查。
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
