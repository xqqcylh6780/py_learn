# -*- coding: utf-8 -*-
"""22 TypeGuard 与 TypeIs

TypeGuard 适合自定义单向缩窄；TypeIs（3.13）可以更自然地描述“如果 True 就是 T，
如果 False 就排除 T”的谓词。两者有不同的兼容性规则。
"""
from typing import TypeGuard, TypeIs

def is_str_list(xs: list[object]) -> TypeGuard[list[str]]:
    return all(isinstance(x, str) for x in xs)

def is_str(x: object) -> TypeIs[str]:
    return isinstance(x, str)

values: list[object] = ['a', 'b']
print(is_str_list(values))
for x in ['hello', 123]:
    print(x, is_str(x))
