# -*- coding: utf-8 -*-
"""30 TYPE_CHECKING、前向引用与循环依赖

TYPE_CHECKING 在静态分析时视为 True，在正常运行时为 False。
它适合只为注解而导入的重依赖/循环依赖，但不要滥用掩盖真实架构问题。
"""
# 学习重点：只在静态阶段需要的导入可放入 TYPE_CHECKING 分支。
# - 前向引用可处理定义顺序，但不能自动解决真实运行时循环依赖。
# - `from __future__ import annotations` 可推迟多数注解求值。
# - 若两个模块在业务执行上互相依赖，应重新划分职责。
# 常见误区：用 TYPE_CHECKING 隐藏运行时确实需要的名称。
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    import decimal  # 示例：仅给静态检查器看到

class Node:
    def __init__(self, parent: 'Node | None' = None) -> None:
        self.parent = parent

print('TYPE_CHECKING at runtime:', TYPE_CHECKING)
print(Node(Node()).parent)
