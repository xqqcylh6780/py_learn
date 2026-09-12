# -*- coding: utf-8 -*-
"""
12 TYPE_CHECKING 与只为类型而存在的导入
=======================================

类型注解有时会制造运行时根本不需要的 import，甚至形成循环导入。
`typing.TYPE_CHECKING` 在正常运行时是 False，而静态类型检查器会把它视为 True。

Python 版本和注解求值策略会影响细节；这里讲最稳妥的结构思想。
"""

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    # 这里的导入只服务静态类型分析。
    from demo_pkg.math_tools import add  # noqa: F401


def show(title):
    print("\n" + "=" * 70)
    print(title)
    print("=" * 70)


show("1. 运行时值")
print("TYPE_CHECKING =", TYPE_CHECKING)

show("2. 用途")
print("当两个模块只因为类型注解互相引用时，可以避免不必要的运行时导入。")

show("3. 注意")
print("如果代码运行时真的要用那个类/函数，就不能只放 TYPE_CHECKING 里。")
print("类型设计不能代替真正的运行时依赖设计。")

show("4. 前向引用")
print("复杂项目还要理解注解何时求值、字符串前向引用和 `from __future__ import annotations` 的版本语义。")
