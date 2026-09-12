# -*- coding: utf-8 -*-
"""09 泛型默认参数（Python 3.13）

PEP 696 在 Python 3.13 为类型参数默认值提供支持。
默认类型参数让常见用法更短，同时仍允许调用者显式特化。
"""
from typing import NoDefault

class Result[T = str]:
    def __init__(self, value: T) -> None:
        self.value = value

type Cache[K = str, V = object] = dict[K, V]

print(Result.__type_params__)
param = Result.__type_params__[0]
print('default:', param.__default__)
print('has_default:', param.has_default())
print('NoDefault sentinel:', NoDefault)
print(Cache)
