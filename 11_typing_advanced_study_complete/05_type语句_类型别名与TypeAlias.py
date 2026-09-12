# -*- coding: utf-8 -*-
"""05 type 语句、类型别名与 TypeAlias

Python 3.12+ 推荐用 type 声明新式类型别名。
类型别名不会创建新的运行时类型；如果需要“品牌类型”，看后面的 NewType。
"""
from typing import TypeAlias, TypeAliasType

# 旧式兼容写法
UserIdList: TypeAlias = list[int]
# Python 3.12+ 新式写法
type Pair[T] = tuple[T, T]

print(UserIdList)
print(Pair)
print('Pair 是 TypeAliasType:', isinstance(Pair, TypeAliasType))
print('Pair[int]:', Pair[int])
