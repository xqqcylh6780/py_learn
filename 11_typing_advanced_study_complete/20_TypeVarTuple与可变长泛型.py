# -*- coding: utf-8 -*-
"""20 TypeVarTuple：类型参数的“可变长参数包”

适合数组 shape、异构元组等“类型参数个数不固定”的抽象。
"""
from typing import TypeVarTuple, Unpack

Ts = TypeVarTuple('Ts')
type Row[*Ts] = tuple[*Ts]

def identity_tuple[*Ts](x: tuple[*Ts]) -> tuple[*Ts]:
    return x

print(identity_tuple((1, 'x', 3.0)))
print(Row[int, str])
