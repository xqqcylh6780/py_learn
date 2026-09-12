# -*- coding: utf-8 -*-
"""09 泛型默认参数（Python 3.13）

PEP 696 在 Python 3.13 为类型参数默认值提供支持。
默认类型参数让常见用法更短，同时仍允许调用者显式特化。
"""
# 学习重点：默认类型参数减少常见调用的显式特化，同时保留高级配置能力。
# - 默认值只在调用者未提供类型参数时生效。
# - NoDefault 可区分“没有默认值”与一个实际类型值。
# - 发布库前要确认 Python 3.13 与检查器对 PEP 696 的支持范围。
# 常见误区：把类型参数默认值误认为函数参数的运行时默认值。
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
