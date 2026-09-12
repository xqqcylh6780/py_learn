# -*- coding: utf-8 -*-
"""13 @runtime_checkable：只做运行时“成员存在性”检查

它不会在 isinstance 时验证完整方法签名或属性类型，所以不能把它当运行时类型验证器。
"""
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
