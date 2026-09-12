# -*- coding: utf-8 -*-
"""06 TypeVar 与泛型函数

泛型的重点是“保持类型之间的关系”，而不是把所有参数都写成 Any。
Python 3.12+ 推荐 def first[T](...) 这种原生类型参数语法。
"""
# 学习重点：TypeVar 记录输入和输出之间必须保持的类型关系。
# - `def first[T](items: list[T]) -> T` 能保留元素的精确类型。
# - 多个位置使用同一 T，表示检查器必须求出一致替换。
# - 若参数和返回值毫无关系，泛型往往不是正确建模方式。
# 常见误区：用 `object -> object` 代替泛型，丢失调用端类型信息。
from typing import TypeVar

T = TypeVar('T')
def first_old(xs: list[T]) -> T:
    return xs[0]

def first[T](xs: list[T]) -> T:
    return xs[0]

print(first([1, 2, 3]))
print(first(['a', 'b']))
print('__type_params__:', first.__type_params__)
