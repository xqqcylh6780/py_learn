# -*- coding: utf-8 -*-
"""30 TYPE_CHECKING、前向引用与循环依赖

TYPE_CHECKING 在静态分析时视为 True，在正常运行时为 False。
它适合只为注解而导入的重依赖/循环依赖，但不要滥用掩盖真实架构问题。
"""
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    import decimal  # 示例：仅给静态检查器看到

class Node:
    def __init__(self, parent: 'Node | None' = None) -> None:
        self.parent = parent

print('TYPE_CHECKING at runtime:', TYPE_CHECKING)
print(Node(Node()).parent)
