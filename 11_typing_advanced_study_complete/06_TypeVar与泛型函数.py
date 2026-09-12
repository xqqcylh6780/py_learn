# -*- coding: utf-8 -*-
"""06 TypeVar 与泛型函数

泛型的重点是“保持类型之间的关系”，而不是把所有参数都写成 Any。
Python 3.12+ 推荐 def first[T](...) 这种原生类型参数语法。
"""
from typing import TypeVar

T = TypeVar('T')
def first_old(xs: list[T]) -> T:
    return xs[0]

def first[T](xs: list[T]) -> T:
    return xs[0]

print(first([1, 2, 3]))
print(first(['a', 'b']))
print('__type_params__:', first.__type_params__)
