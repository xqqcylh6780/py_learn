# -*- coding: utf-8 -*-
"""01 类型提示的边界与心智模型

核心结论：类型提示首先服务于静态分析、人和 IDE；Python 运行时通常不会替你检查类型。
类型系统是“渐进式”的：可以从局部开始，不要求整个项目一次性类型化。
"""
# 学习重点：注解主要是一份可被工具读取的接口说明。
# - 解释器通常不会拒绝传入错误类型；是否检查取决于静态检查器或框架。
# - 注解对象可通过 __annotations__ 和 get_type_hints() 读取。
# - 渐进式类型允许先标注公共边界，再逐步覆盖内部实现。
# 常见误区：把“已写注解”等同于“运行时已经安全”。
from typing import get_type_hints

def add(a: int, b: int) -> int:
    return a + b

print('annotations:', add.__annotations__)
print('resolved:', get_type_hints(add))
print('add(1, 2) =', add(1, 2))
print("运行时甚至允许 add('a', 'b'):", add('a', 'b'))
print('所以：注解不是运行时参数验证器。')
print('静态检查器会在运行前指出不匹配；运行时校验需要你自己写或使用专门库。')
