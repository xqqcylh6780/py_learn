# -*- coding: utf-8 -*-
"""31 dataclass_transform：告诉检查器“这个框架会生成类似 dataclass 的方法”

这是给 ORM、校验模型、数据模型框架作者的高级能力。装饰器本身不替你生成 __init__；
它描述的是静态转换约定。
"""
from typing import dataclass_transform

@dataclass_transform()
def model(cls):
    # 这里只做一个极简运行时标记；真实框架会生成方法/字段逻辑。
    cls.__model__ = True
    return cls

@model
class User:
    name: str
    age: int

print(User.__annotations__)
print(User.__model__)
print('类型检查器可把 @model 理解为 dataclass-like 转换。')
