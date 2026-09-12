# -*- coding: utf-8 -*-
"""19 @overload：描述输入与返回类型之间的对应关系

overload 声明只给类型检查器看；后面必须有一个真正的运行时实现。
"""
from typing import overload, get_overloads

@overload
def normalize(x: str) -> str: ...
@overload
def normalize(x: bytes) -> bytes: ...
def normalize(x: str | bytes) -> str | bytes:
    return x.strip()

print(normalize('  hi  '))
print(normalize(b'  hi  '))
print('overload count:', len(get_overloads(normalize)))
