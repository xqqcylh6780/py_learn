# -*- coding: utf-8 -*-
"""31 dataclass_transform：告诉检查器“这个框架会生成类似 dataclass 的方法”

这是给 ORM、校验模型、数据模型框架作者的高级能力。装饰器本身不替你生成 __init__；
它描述的是静态转换约定。
"""
# 学习重点：dataclass_transform 是框架与检查器之间的约定。
# - 它可描述装饰器、基类或元类会生成 __init__、比较方法等行为。
# - 参数可声明字段描述器、默认值规则和关键字参数策略。
# - 框架仍必须在运行时真正实现所承诺的转换。
# 常见误区：只加装饰器标记却未生成对应方法。
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
