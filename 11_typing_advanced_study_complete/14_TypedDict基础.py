# -*- coding: utf-8 -*-
"""14 TypedDict：给“固定键结构的 dict”加类型

TypedDict 主要是静态概念；运行时得到的仍是普通 dict。
"""
# 学习重点：TypedDict 为字典的键集合和各键值类型建立静态契约。
# - 它适合 JSON 风格记录、配置片段和逐步类型化的旧字典接口。
# - 运行时对象仍是 dict，不会自动拒绝缺失键或多余键。
# - 需要验证外部输入时，仍应先解析和校验再赋予 TypedDict 类型。
# 常见误区：把 TypedDict 当成 dataclass 或运行时 schema。
from typing import TypedDict

class UserRow(TypedDict):
    id: int
    name: str

u: UserRow = {'id': 1, 'name': 'Alice'}
print(u, type(u))
print(UserRow.__required_keys__)
print(UserRow.__optional_keys__)
