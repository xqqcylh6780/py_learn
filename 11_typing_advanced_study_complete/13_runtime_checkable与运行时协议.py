# -*- coding: utf-8 -*-
"""13 @runtime_checkable：只做运行时“成员存在性”检查

它不会在 isinstance 时验证完整方法签名或属性类型，所以不能把它当运行时类型验证器。
"""
# 学习重点：runtime_checkable 只支持粗粒度的成员存在性检查。
# - isinstance() 不会验证方法参数、返回类型或可变属性的精确类型。
# - 它适合轻量能力探测，不能替代数据校验或安全边界检查。
# - 需要严格运行时契约时，应编写显式验证逻辑。
# 常见误区：静态上满足 Protocol，就假设任意运行时对象都完全可靠。
from typing import Protocol, runtime_checkable, is_protocol, get_protocol_members

@runtime_checkable
class HasName(Protocol):
    name: str

class User:
    name = 'Alice'

print(is_protocol(HasName))
print(get_protocol_members(HasName))
print(isinstance(User(), HasName))
print('runtime protocol check 有意保持浅层；签名兼容仍主要由静态检查器负责。')
