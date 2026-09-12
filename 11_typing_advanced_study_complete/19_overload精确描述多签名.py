# -*- coding: utf-8 -*-
"""19 @overload：描述输入与返回类型之间的对应关系

overload 声明只给类型检查器看；后面必须有一个真正的运行时实现。
"""
# 学习重点：overload 用多组调用签名描述输入与输出的对应关系。
# - 所有 overload 分支之后必须有一个能处理全部情况的运行时实现。
# - 分支应互斥或按更具体到更宽泛排列，避免调用匹配歧义。
# - 若返回值与输入无对应关系，普通联合类型通常更简单。
# 常见误区：给每个分支写运行时代码；装饰过的声明不会作为实现执行。
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
