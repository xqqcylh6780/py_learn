# -*- coding: utf-8 -*-
"""14 TypedDict：给“固定键结构的 dict”加类型

TypedDict 主要是静态概念；运行时得到的仍是普通 dict。
"""
from typing import TypedDict

class UserRow(TypedDict):
    id: int
    name: str

u: UserRow = {'id': 1, 'name': 'Alice'}
print(u, type(u))
print(UserRow.__required_keys__)
print(UserRow.__optional_keys__)
