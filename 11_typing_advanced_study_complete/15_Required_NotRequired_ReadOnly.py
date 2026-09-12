# -*- coding: utf-8 -*-
"""15 TypedDict：Required、NotRequired、ReadOnly

NotRequired/Required 控制键是否必须存在；ReadOnly（3.13）告诉类型检查器该项不能被写入。
"""
from typing import TypedDict, Required, NotRequired, ReadOnly

class Config(TypedDict, total=False):
    host: Required[str]
    port: int
    token: NotRequired[str]
    version: ReadOnly[int]

print('required:', Config.__required_keys__)
print('optional:', Config.__optional_keys__)
print('annotations:', Config.__annotations__)
print('ReadOnly 是静态约束；普通 dict 运行时本身不会冻结该键。')
