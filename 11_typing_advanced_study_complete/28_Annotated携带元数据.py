# -*- coding: utf-8 -*-
"""28 Annotated：类型 + 附加元数据

Annotated[T, meta...] 不会自动赋予 meta 统一语义；框架可以自行解释这些元数据。
"""
from typing import Annotated, get_args, get_origin

UserAge = Annotated[int, 'min=0', 'max=150']
print(UserAge)
print('origin:', get_origin(UserAge))
print('args:', get_args(UserAge))

def register(age: UserAge) -> None:
    print(age)
register(20)
