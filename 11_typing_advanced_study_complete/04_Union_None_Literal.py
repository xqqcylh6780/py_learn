# -*- coding: utf-8 -*-
"""04 Union、None 与 Literal

T | None 表示值可以是 T 或 None；它不表示参数自动拥有默认值。
Literal 用来表达“只能是这些具体值”。
"""
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
