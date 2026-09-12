# -*- coding: utf-8 -*-
"""05 type 语句、类型别名与 TypeAlias

Python 3.12+ 推荐用 type 声明新式类型别名。
类型别名不会创建新的运行时类型；如果需要“品牌类型”，看后面的 NewType。
"""
# 学习重点：类型别名为复杂类型命名，但不会建立新的业务身份。
# - Python 3.12+ 的 type 语句能明确区分别名与普通赋值。
# - 旧版本可使用 TypeAlias 保持意图清晰。
# - 需要阻止 UserId 与 OrderId 混用时，应使用 NewType 或真实类。
# 常见误区：把别名当作运行时构造器或独立子类。
from typing import TypeAlias, TypeAliasType

# 旧式兼容写法
UserIdList: TypeAlias = list[int]
# Python 3.12+ 新式写法
type Pair[T] = tuple[T, T]

print(UserIdList)
print(Pair)
print('Pair 是 TypeAliasType:', isinstance(Pair, TypeAliasType))
print('Pair[int]:', Pair[int])
