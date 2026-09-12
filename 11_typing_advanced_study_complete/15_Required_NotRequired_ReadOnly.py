# -*- coding: utf-8 -*-
"""15 TypedDict：Required、NotRequired、ReadOnly

NotRequired/Required 控制键是否必须存在；ReadOnly（3.13）告诉类型检查器该项不能被写入。
"""
# 学习重点：键是否必需、能否写入和键值类型是三个独立维度。
# - total=False 让默认键可选，Required 可单独恢复某个必需键。
# - NotRequired 可在 total=True 中标记少量可选键。
# - ReadOnly 约束静态写入，不会冻结运行时字典。
# 常见误区：把 Optional[T] 理解为“键可以不存在”；它仅表示值可为 None。
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
