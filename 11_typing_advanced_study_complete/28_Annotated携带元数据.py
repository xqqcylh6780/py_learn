# -*- coding: utf-8 -*-
"""28 Annotated：类型 + 附加元数据

Annotated[T, meta...] 不会自动赋予 meta 统一语义；框架可以自行解释这些元数据。
"""
# 学习重点：Annotated 把基础类型与框架可解释的元数据放在同一注解中。
# - 不认识元数据的工具应仍把 Annotated[T, ...] 视为 T。
# - 校验、依赖注入和序列化框架可以约定自己的元数据协议。
# - 元数据本身不会自动执行，必须由消费方读取并实施规则。
# 常见误区：写了 min/max 文本就认为解释器会自动校验。
from typing import Annotated, get_args, get_origin

UserAge = Annotated[int, 'min=0', 'max=150']
print(UserAge)
print('origin:', get_origin(UserAge))
print('args:', get_args(UserAge))

def register(age: UserAge) -> None:
    print(age)
register(20)
