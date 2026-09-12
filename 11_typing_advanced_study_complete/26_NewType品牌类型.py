# -*- coding: utf-8 -*-
"""26 NewType：给相同底层类型增加静态语义身份"""
from typing import NewType

UserId = NewType('UserId', int)
OrderId = NewType('OrderId', int)

def load_user(uid: UserId) -> str:
    return f'user:{uid}'

uid = UserId(10)
print(load_user(uid))
print(type(uid), uid == 10)
print('NewType 运行时开销很小；价值主要在静态阶段防止把不同 ID 混用。')
