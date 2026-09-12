# -*- coding: utf-8 -*-
"""22 TypeGuard 与 TypeIs

TypeGuard 适合自定义单向缩窄；TypeIs（3.13）可以更自然地描述“如果 True 就是 T，
如果 False 就排除 T”的谓词。两者有不同的兼容性规则。
"""
# 学习重点：自定义谓词可把运行时判断结果传达给静态检查器。
# - TypeGuard 在 True 分支缩窄，适合目标类型不严格是输入类型子类型的情况。
# - TypeIs 要求安全的子类型关系，并能同时改进 True 与 False 两个分支。
# - 谓词实现必须诚实，否则会制造静态上安全、运行时失败的代码。
# 常见误区：为了消除报错而返回恒定 True。
from typing import TypeGuard, TypeIs

def is_str_list(xs: list[object]) -> TypeGuard[list[str]]:
    return all(isinstance(x, str) for x in xs)

def is_str(x: object) -> TypeIs[str]:
    return isinstance(x, str)

values: list[object] = ['a', 'b']
print(is_str_list(values))
for x in ['hello', 123]:
    print(x, is_str(x))
