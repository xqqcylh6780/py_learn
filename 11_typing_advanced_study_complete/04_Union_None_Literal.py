# -*- coding: utf-8 -*-
"""04 Union、None 与 Literal

T | None 表示值可以是 T 或 None；它不表示参数自动拥有默认值。
Literal 用来表达“只能是这些具体值”。
"""
# 学习重点：联合类型表达多种合法状态，Literal 表达有限取值集合。
# - T | None 要在使用前处理 None；默认值仍需在函数签名中显式给出。
# - Literal 适合模式、状态和命令名，不适合不断增长的业务数据。
# - 分支判断可以让检查器自动缩窄联合类型。
# 常见误区：使用 str 代替有限状态，导致拼写错误无法被检查。
from typing import Literal, get_args

Mode = Literal['read', 'write']

def open_like(path: str, mode: Mode = 'read') -> str:
    return f'{mode}:{path}'

def parse(text: str) -> int | None:
    try:
        return int(text)
    except ValueError:
        return None

print(open_like('a.txt'))
print(parse('42'), parse('x'))
print('Mode literals:', get_args(Mode))
