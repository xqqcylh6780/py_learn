# -*- coding: utf-8 -*-
"""26 NewType：给相同底层类型增加静态语义身份

NewType 可区分 UserId、OrderId 这类底层都是 int 的业务标识，防止接口间
误传。调用 NewType 在运行时几乎不产生包装成本，值仍是原底层对象。

它不提供运行时校验、方法或不变量。需要验证格式或封装行为时，应使用真实
类、dataclass 或显式解析函数。
"""
from typing import NewType

UserId = NewType('UserId', int)
OrderId = NewType('OrderId', int)

def load_user(uid: UserId) -> str:
    return f'user:{uid}'

uid = UserId(10)
print(load_user(uid))
print(type(uid), uid == 10)
print('NewType 运行时开销很小；价值主要在静态阶段防止把不同 ID 混用。')
