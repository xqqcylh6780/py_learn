# -*- coding: utf-8 -*-
"""20 TypeVarTuple：类型参数的“可变长参数包”

适合数组 shape、异构元组等“类型参数个数不固定”的抽象。
"""
# 学习重点：TypeVarTuple 捕获数量不固定的一组类型参数。
# - 它适合异构元组和带 shape 类型的数组接口。
# - 使用 Unpack[Ts] 或新语法 *Ts 展开参数包。
# - 一个类型参数列表中通常只能有一个可变长参数包。
# 常见误区：把 TypeVarTuple 当成运行时 tuple 值或普通 *args。
from typing import TypeVarTuple, Unpack

Ts = TypeVarTuple('Ts')
type Row[*Ts] = tuple[*Ts]

def identity_tuple[*Ts](x: tuple[*Ts]) -> tuple[*Ts]:
    return x

print(identity_tuple((1, 'x', 3.0)))
print(Row[int, str])
